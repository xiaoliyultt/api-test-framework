import yaml
import requests
from utils import load_config

config = load_config()
print(f"base_url:{config['base_url']}")
print(f"timeout:{config['timeout']}")

base_url = config['base_url']
timeout = config['timeout']

response = requests.get(f"{base_url}/get",timeout=timeout)

print(f"状态码：{response.status_code}")
print(f"返回内容:{response.text[:200]}")
#print(f"完整返回内容:${response}")
assert response.status_code == 200
