#-*- coding: utf-8 -*- 

'''
부동산 거래 통계 데이터 호출
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

'''
1. 수신 데이터 구조(연도별, 거래주체별 거래건수)

조사년도, 거래주체별_합계, 개인->개인, 개인->법인, 개인->기타,
법인->개인, 법인->법인, 법인->기타, 기타->개인, 기타->법인,
기타->기타 부동산 거래 건수

2. 수신 데이터 구조(연도별, 건물 유형별 거래건수)

조사년도, 건물유형별_합계, 주거용 소계, 단독주택, 다가구주택,
다세대주택, 연립주택, 아파트, 상업업무용, 공업용,
기타건물 부동산 거래 건수 

3. 거래 원인별 부동산 거래건수 
조사년도, 거래원인별_합계, 매매, 판결, 교환,
증여, 분양권, 기타 부동산 거래 건수

4. 월별 부동산 거래건수
조사월, 부동산 거래건수

'''

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
