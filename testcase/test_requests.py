import requests
import logging
import pytest
import json


class TestRequests(object):
    logging.basicConfig()

    def test_get(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))

    def test_post(self):
        r = requests.post(self.url,
                          json={"a": 1, "b": "string corntent"},
                          headers={"a": "1", "b": "b2"},
                          proxies={"https": "127.0.0.1:7778", "http": "127.0.0.1:7778"},
                          verify=False)
        logging.info(r.url)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))

    def test_cookies(self):
        r = requests.get("", cookies={"a": "1", "b": "string content"})
        logging.info(r.text)

    def test_xueqiu_qoute(self):
        pass
