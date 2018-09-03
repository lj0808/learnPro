import requests
import selenium


r = requests.get('http://baidu.com ')
r.status_code
r.text
r.cookies['ret']