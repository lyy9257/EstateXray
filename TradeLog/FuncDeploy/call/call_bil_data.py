#-*- coding: utf-8 -*- 

'''
다세대(빌라), 단독주택 데이터 호출
For GCP Deploy
Start Function : cloud_deploy_start
'''

import configparser
import gc
import json
import os
import pandas as pd
import sys
import pymysql
import requests
import xmltodict

from datetime import datetime
from sqlalchemy import create_engine

# 루틴 Class
# 필요 함수들은 여기서 모여서 시작.
class Routine():

    ## 초기화
    def __init__(self):

    ## 지역코드 데이터 호출
    def query_areacode(self):
        return result

    ## 데이터 크롤링
    def call_data(self):
        return result
        
    ## 전처리
    def refine(self, rawdata):
        return result
        
    ## 거래로그 저장
    def save_tradelog(self, data, code):
        return True

    ## run
    def run(self):
        return True

# GCP Start Function 
# GCP Function에 Deploy할 경우 사용 
def cloud_deploy_start():
    return True

# Local Start Function
# 로컬에서 시작할 경우 사용
def local_start():
    return True

# 로컬 테스트용
if __name__ == '__main__':
