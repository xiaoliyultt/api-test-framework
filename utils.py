import yaml
import requests
def load_config():
    with open('config.yaml','r',encoding="utf-8") as f:
        return yaml.safe_load(f)

class APIClient:
    def __init__(self):
        config = load_config()
        self.base_url = config['test_url']
        self.timeout = config.get('timeout',30)
        self.token= None

    def set_token(self,token):
        self.token = token

    def _get_headers(self):
        if self.token :
            return {"Authorization" : f"Bearer {self.token}"}
        return {}


    def get(self,endpoint, **kwargs):
        url= f"{self.base_url}{endpoint}"
        kwargs.setdefault('timeout', self.timeout)
        headers = self._get_headers()
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        kwargs['headers'] = headers
        return requests.get(url, **kwargs)

    def post(self,endpoint, **kwargs):
        url= f"{self.base_url}{endpoint}"
        kwargs.setdefault('timeout',self.timeout)
        headers = self._get_headers()
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        kwargs['headers'] = headers
        return requests.post(url, **kwargs)

    def put(self, endpoint, **kwargs):
        url= f"{self.base_url}{endpoint}"
        kwargs.setdefault('timeout', self.timeout)
        headers = self._get_headers()
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        kwargs['headers'] = headers
        return requests.put(url, **kwargs)

    def delete(self, endpoint, **kwargs):
        url=f"{self.base_url}{endpoint}"
        kwargs.setdefault('timeout',self.timeout)
        headers = self._get_headers()
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        kwargs['headers'] = headers
        return requests.delete(url, **kwargs)



def  assert_response(response, expected_status_code):
    print(f"状态码: {response.status_code}")
    response_test = response.text[:500] if len(response.text) > 500 else response.text
    print(f"响应体：{response_test}")
    assert response.status_code ==expected_status_code , f"期望{expected_status_code},实际{response.status_code}"
