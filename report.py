from codecs import ignore_errors
from email.policy import strict
import requests
import json
import logging
import time, datetime
import urllib3
import base64



logging.basicConfig(filename='health_report.log',level=logging.INFO)
def report(sessionID):
    urllib3.disable_warnings()
    #logging.captureWarnings(True)
    url = 'https://zhxg.whut.edu.cn/yqtjwx/monitorRegister'
    header = {
        'Host': 'zhxg.whut.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '460',
        'Cookie': 'JSESSIONID=' + sessionID,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'X-Tag': 'flyio',
        'content-type': 'application/json',
        'encode': 'true',
        'Referer': 'https://servicewechat.com/wxa0738e54aae84423/21/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    '''data = {"equipments": "microsoft-microsoft","diagnosisName": "", "relationWithOwn": "", "currentAddress": "湖北省武汉市洪山区武汉理工大学", "remark": "",
                  "healthInfo": "正常", "isDiagnosis": 0, "isFever": 0, "isInSchool": 1, "isLeaveChengdu": 0,
                  "isSymptom": "0", "temperature": "36°C以下", "province": "湖北省", "city": "武汉市", "county": "洪山区"}'''
    header['Cookie'] = 'JSESSIONID=' + sessionID
    data1 = 'eyJlcXVpcG1lbnRzIjoibWljcm9zb2Z0LW1pY3Jvc29mdCIsImRpYWdub3Npc05hbWUiOiIiLCJyZWxhdGlvbldpdGhPd24iOiIiLCJjdXJyZW50QWRkcmVzcyI6Iua5luWMl+ecgeatpuaxieW4guaxn+WyuOWMuuS4reWxseWkp+mBkzg5MOWPtyIsInJlbWFyayI6IiIsImhlYWx0aEluZm8iOiLmraPluLgiLCJpc0RpYWdub3NpcyI6MCwiaXNGZXZlciI6MCwiaXNJblNjaG9vbCI6MCwiaXNMZWF2ZUNoZW5nZHUiOjAsImlzU3ltcHRvbSI6IjAiLCJ0ZW1wZXJhdHVyZSI6IjM2wrBD5Lul5LiLIiwicHJvdmluY2UiOiLmuZbljJfnnIEiLCJjaXR5Ijoi5q2m5rGJ5biCIiwiY291bnR5Ijoi5rGf5bK45Yy6In0='  #.encode('utf-8')
    res = requests.post(url, headers=header, data=data1, verify=False,)
    logging.info(res)
    #print(type(res))
    res_json = res.json()
    nowtime = str(datetime.datetime.now()).split(".")[0]
    print(res_json)
    if res_json['status'] == True:
        print(nowtime + ": '" + sessionID + "'报送成功, 返回信息为" + str(res_json))
        logging.info(nowtime + ": '" + sessionID + "'报送成功, 返回信息为" + str(res_json))
    elif res_json['status'] == False:
        print(nowtime + ": '" + sessionID + "'报送失败, 返回信息为" + str(res_json))
        logging.info(nowtime + ": '" + sessionID + "'报送失败, 返回信息为" + str(res_json))
    else:
        print(nowtime + ": '" + sessionID + "'报送过程中发生未知错误，返回值为" + str(res_json))
        logging.info(nowtime + ": '" + sessionID + "'报送失败, 返回信息为" + str(res_json))
    #except:
       #pass'''

