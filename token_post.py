import requests


# 获取token函数
        
url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
data = {
    "app_id": "×××××××××××××××××",
    "app_secret": "×××××××××××××××××"
    }
headers ={'Content-Type':'application/json,charset=utf-8'}
#发送post请求
req = requests.post(url,data,headers)
# 将获取的token打印
print (req.json())
#提取token字段
tokenValue = req.json()['tenant_access_token']
strlist = 'Bearer '+tokenValue
print(req.json()['tenant_access_token'])
print(strlist)
