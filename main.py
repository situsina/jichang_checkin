import requests, json, re, os

session = requests.session()
# 机场的地址
url = os.environ.get('URL')
# 配置用户名（一般是邮箱）
email = os.environ.get('EMAIL')
# 配置用户名对应的密码 和上面的email对应上
passwd = os.environ.get('PASSWD')

login_url = '{}/auth/login'.format(url)
check_url = '{}/user/checkin'.format(url)

header = {
        'origin': url,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
data = {
        'email': email,
        'passwd': passwd
}
try:
    print('进行登录...')
    response = json.loads(session.post(url=login_url,headers=header,data=data).text)
    print(response['msg'])
    # 进行签到
    result = json.loads(session.post(url=check_url,headers=header).text)
    print(result['msg'])
    content = result['msg']


# 机场的地址
url1 = os.environ.get('URL1')
# 配置用户名（一般是邮箱）
email1 = os.environ.get('EMAIL1')
# 配置用户名对应的密码 和上面的email对应上
passwd1 = os.environ.get('PASSWD1')

login_url = '{}/auth/login'.format(url1)
check_url = '{}/user/checkin'.format(url1)

header = {
        'origin': url1,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
data = {
        'email': email1,
        'passwd': passwd1
}
try:
    print('进行登录...')
    response = json.loads(session.post(url=login_url,headers=header,data=data).text)
    print(response['msg'])
    # 进行签到
    result = json.loads(session.post(url=check_url,headers=header).text)
    print(result['msg'])
    content = result['msg']
