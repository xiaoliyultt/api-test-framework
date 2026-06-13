# 这是一个反面教材 - 充满坏味道的测试脚本
import requests
import time
from utils import load_config
from utils import APIClient
from utils import assert_response


config = load_config()

print(config['test_url'])

api= APIClient()

# 测试1：用户登录
#url1 = f"{config['test_url']}/login"
payload1 = {"username": "{config['username']}", "password": "config['password']"}
r1 = api.post('/login', json=payload1)
'''
print(r1.status_code)
print(r1.text)
assert r1.status_code == 200
'''
assert_response(r1,200)
token = r1.json()["token"]
api.set_token(token)

# 测试2：查询订单
#url2 = f"{config['test_url']}/order"
'''
headers2 = {"Authorization": f"Bearer {token}"}
r2 = api.get('/order', headers=headers2)
'''
r2 = api.get('/order')

'''
print(r2.status_code)
print(r2.text)
assert r2.status_code == 200
'''
assert_response(r2,200)


# 测试3：创建订单
#url3 = f"{config['test_url']}/order"
payload3 = {"product_id": 1001, "quantity": 2}
'''
r3 = api.post('/order', json=payload3, headers=headers2)
'''
r3 = api.post('/order',json=payload3)
'''
print(r3.status_code)
print(r3.text)
assert r3.status_code == 201
'''
assert_response(r3,201)

# 测试4：查询订单详情
order_id = r3.json()["order_id"]
#url4 = f"{config['test_url']}/order/{order_id}"
#r4 = api.get(f'/order/{order_id}', headers=headers2)
r4 = api.get(f'/order/{order_id}')
'''
print(r4.status_code)
print(r4.text)
assert r4.status_code == 200
'''
assert_response(r4,200)

# 硬编码等待
time.sleep(2)

# 测试5：删除订单
#url5 = f"{config['test_url']}/order/{order_id}"
#r5 = api.delete(f'/order/{order_id}', headers=headers2)
r5 = api.delete(f'/order/{order_id}')
'''
print(r5.status_code)
assert r5.status_code == 204
'''
assert_response(r5,204)

print("所有测试通过")