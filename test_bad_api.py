# 这是一个反面教材 - 充满坏味道的测试脚本
import requests
import time
from utils import load_config
from utils import APIClient
from utils import assert_response
import pytest


config = load_config()

print(config['test_url'])



@pytest.fixture
def api():
    client = APIClient()
    client.set_token("fake_token")
    return client


def test_get_post(api):
    r = api.get("/posts/1")
    assert_response(r,200)

#r1 = api.get("/posts/1")
#assert_response(r1, 200)

def test_create_post(api):
    r = api.post("/posts", json={"title": "test", "body": "hello", "userId": 1})
    assert_response(r,201)

#r2 = api.post("/posts", json={"title": "test", "body": "hello", "userId": 1})
#assert_response(r2, 201)


#print("所有测试通过")

def test_update_post(api):
    r = api.put("/posts/1", json={"id": 1, "title": "updated", "body": "new", "userId": 1})
    assert_response(r,200)


