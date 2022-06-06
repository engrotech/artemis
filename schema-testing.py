
from distutils.command.config import config
import os
# from dotenv import load_dotenv
import schemathesis
import json
import requests
import configparser

from unittest import TestCase

from schemathesis import DataGenerationMethod
from schemathesis.checks import not_a_server_error, response_headers_conformance, content_type_conformance, response_schema_conformance
from hypothesis import settings, Phase, HealthCheck
import yaml

# load_dotenv()
# BASE_URL = os.getenv('BASE_URL')
# ENDPOINT = os.getenv('ENDPOINT')
# AUTH = os.getenv('AUTH')
# @settings(max_examples=1000)



# config = configparser.ConfigParser()
# config.read('config.ini')

# BASE_URL = config['DEFAULTS']['BASE_URL']
# ENDPOINT = config['DEFAULTS']['ENDPOINT']
# AUTH = config['DEFAULTS']['AUTH']
with open('config.yaml') as file:
    config = yaml.full_load(file)

BASE_URL = config['BASE_URL']
ENDPOINT = config['ENDPOINT']
AUTH = config['AUTH']
schema = schemathesis.from_uri(BASE_URL, validate_schema=False)
# schema = schemathesis.from_path('/home/arijit/Project/API_Test/data/openapi-fast.json', base_url="http://127.0.0.1:8000")
# schema_negative =  schemathesis.from_uri(BASE_URL, validate_schema=False, data_generation_methods=[DataGenerationMethod.negative])

# , data_generation_methods=[DataGenerationMethod.negative]
# schema = schemathesis.from_uri("https://example.schemathesis.io/openapi.json", base_url="https://example.schemathesis.io", validate_schema=False, skip_deprecated_operations=True)
# openapi_data = open('data/openapi-fast.json', 'r')


# @schema.parametrize(endpoint=ENDPOINT)
# def call_validation(case):
#     schemathesis.fixups.install()
#     case.call_and_validate()
    
    # operation = schema['/add']
    # strategy = operation.as_strategy()
    # print(strategy.example())

# Custom Tests
@schema.parametrize(endpoint=ENDPOINT)
@settings(suppress_health_check=(HealthCheck.too_slow,HealthCheck.filter_too_much,))
def custom_test1(case):
    response = case.call()
    case.validate_response(response, checks=(not_a_server_error, response_headers_conformance, response_schema_conformance))
    # case.call_and_validate(headers={"Authorization" : "Token NJNINGJHZJCTNDC5NY0ZZWRJLTHKOWQTOTAYNZC3NMI3YJI1"})
# 127.0.0.1:8000

