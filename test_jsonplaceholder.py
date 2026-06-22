import pytest
from utils import APIClient, assert_response, assert_schema


post_schema = {
    "type" : "object",
    "properties" : {
        "userId" : {"type": "integer"},
        "id": {"type": "integer"},
        "title" : {"type": "string"},
        "body": {"type": "string"}
    },
    "required" : ["userId", "id", "title", "body"]
}


# 这是一个 fixture，每个测试函数会自动接收它
@pytest.fixture
def api():
    """创建一个 API 客户端，并设置假token"""
    client = APIClient()
    client.set_token("fake_token_for_testing")
    return client

# 测试1：GET 请求 - 获取单个帖子
def test_get_single_post(api):
    response = api.get("/posts/1")
    assert_response(response, 200)
    assert_schema(response, post_schema)

# 测试2：GET 请求 - 获取帖子列表
def test_get_all_posts(api):
    response = api.get("/posts")
    assert_response(response, 200)

# 测试3：POST 请求 - 创建新帖子
def test_create_post(api):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = api.post("/posts", json=payload)
    assert_response(response, 201)   # jsonplaceholder 对于创建返回 201

# 测试4：PUT 请求 - 更新帖子
def test_update_post(api):
    payload = {"id": 1, "title": "updated", "body": "new content", "userId": 1}
    response = api.put("/posts/1", json=payload)
    assert_response(response, 200)

# 测试5：DELETE 请求 - 删除帖子
def test_delete_post(api):
    response = api.delete("/posts/1")
    assert_response(response, 200)   # jsonplaceholder 删除返回 200


def test_get_post_1(api):
    assert_response(api.get("/posts/1"), 200)

def test_get_post_2(api):
    assert_response(api.get("/posts/2"), 200)

def test_get_post_3(api):
    assert_response(api.get("/posts/3"), 200)

@pytest.mark.parametrize("post_id", [1,2,3])
def test_get_post_by_id(api,post_id):
    response = api.get(f"/posts/{post_id}")
    assert_response(response, 200)

@pytest.mark.parametrize("endpoint, expected_status",[("/posts/1",200), ("/posts/999", 404), ("/invalid-path", 404), ("/posts", 200),])
def test_api_response(api, endpoint,expected_status):
    response = api.get(endpoint)
    assert_response(response, expected_status)