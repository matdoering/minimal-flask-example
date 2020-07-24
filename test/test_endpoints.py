import os
import requests
from openapi_spec_validator import validate_spec_url

def test_blueprint_x_test(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'path_for_blueprint_x', 'test')
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert 'msg' in json
    assert json['msg'] == "I'm the test endpoint from blueprint_x."

def test_blueprint_y_test(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'path_for_blueprint_y', 'test')
    response = requests.get(endpoint)
    assert response.status_code == 200
    json = response.json()
    assert 'msg' in json
    assert json['msg'] == "I'm the test endpoint from blueprint_y."

def test_blueprint_x_plus(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'path_for_blueprint_x', 'plus')
    payload = {'number': 5}
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 200
    json = response.json()
    assert 'msg' in json
    assert json['msg'] == "Your result is: '10'"

def test_blueprint_x_minus(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'path_for_blueprint_y', 'minus')
    payload = {'number': 1000}
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 200
    json = response.json()
    assert 'msg' in json
    assert json['msg'] == "Your result is: '0'"

def test_swagger_specification(host):
    endpoint = os.path.join(host, 'api', 'swagger.json')
    validate_spec_url(endpoint)
    # use https://editor.swagger.io/ to fix issues
