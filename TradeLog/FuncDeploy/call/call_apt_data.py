'''
아파트 거래 히스토리 쿼리 
'''

import pandas as pd
import configparser
import pymysql

### Read config about database
config = configparser.ConfigParser()
config.read('config.cfg', encoding = 'utf-8')

db_ip = config.get('MYSQL', 'DB_IP')
db_port = config.get('MYSQL', 'DB_PORT')
db_id = config.get('MYSQL', 'DB_ID')
db_pw = config.get('MYSQL', 'DB_PW')

# 아파트 거래내역 검색
def search_trade_history(request):

    # json 호출
    request_json = request.get_json()
    
    # 호출 데이터 길이 Syntax
    # 만약에 args 없으면 X
    req_size_syntax = ''

    # argument parsing    
    if request.args:
        area_big = request.args.get('area_big')
        area_small = request.args.get('area_small')
        apart_name = request.args.get('apart_name')

     
        if request.args.get('reqSize') != None:
            req_size = request.args.get('reqSize')
            req_size_syntax = 'LIMIT (0, %s)'

    # json parsing
    if request_json:
        area_big = request_json['area_big']
        area_small = request_json['area_small']
        apart_name = request_json['apart_name']

        if request_json['reqSize']:
            req_size = request_json['reqSize']
            req_size_syntax = """
                LIMIT (0, %(reqSize)s)
            """ %{
                'reqSize' : req_size
            }

    
    ### 저장할 데이터베이스 호출(pymysql)
    db_conn = pymysql.connect(
        host = db_ip,
        user = db_id,
        password = db_pw,
        db = 'apart',
        charset = 'utf8'
    )

    sql_syntax = """
        SELECT 년, 월, 일, 전용면적, 층, 평수, 평당가, 거래금액
        FROM apart.tradelog_%(area_big)s
        WHERE 법정동읍면동코드 = '%(area_small)s' and 아파트 = '%(apart_name)s
        %(req_size_syntax)';
    """ %{
        'area_big' : area_big,
        'area_small' : area_small,
        'apart_name' : apart_name,
        'req_size_syntax' : req_size_syntax
    }

    result = pd.read_sql(sql_syntax, db_conn).to_json(
        orient='records', indent=4, force_ascii=False
    )
    
    return result
