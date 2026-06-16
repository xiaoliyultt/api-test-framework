import yaml
import requests
import logging

def load_config():
    with open('config.yaml','r',encoding="utf-8") as f:
        return yaml.safe_load(f)



#配置日志
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler('test.log' , encoding ='utf-8'), #输出到文件
        logging.StreamHandler()  #同时也输出到控制台
    ]
)
logger = logging.getLogger(__name__)
logger.warning("日志模块已加载，这条应该写入文件")




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

        #添加日志
        logger.info(f"发送 GET 请求：{url}")
        logger.debug(f"请求头: {headers}")

        response = requests.get(url, **kwargs)

        logger.info(f"收到响应: {response.status_code}")
        logger.debug(f"响应体: {response.text[:500]}")

        return response

    def post(self,endpoint, **kwargs):
        url= f"{self.base_url}{endpoint}"
        kwargs.setdefault('timeout',self.timeout)
        headers = self._get_headers()
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        kwargs['headers'] = headers

        # 添加日志
        logger.info(f"发送 POST 请求：{url}")
        logger.debug(f"请求头: {headers}")

        response = requests.post(url, **kwargs)

        logger.info(f"收到响应: {response.status_code}")
        logger.info(f"响应体: {response.text[:500]}")

        return response


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
    logger.info(f"开始断言: 期望状态码 {expected_status_code}")  # 临时加这行
    print(f"状态码: {response.status_code}")
    response_test = response.text[:500] if len(response.text) > 500 else response.text
    print(f"响应体：{response_test}")

    if response.status_code != expected_status_code:
        logger.error(f"断言失败-- 期望: {expected_status_code}, 实际: {response.status_code}")
        logger.error(f"响应体: {response.text[:500]}")


    assert response.status_code ==expected_status_code , f"期望{expected_status_code},实际{response.status_code}"





