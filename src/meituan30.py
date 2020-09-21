import requests
import time
import schedule
import smtplib
from email.mime.text import MIMEText
from email.header import Header

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi K30 Pro Build/QKQ1.200419.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36; unicom{version:android@7.0400,desmobile:13226408930};devicetype{deviceBrand:Xiaomi,deviceModel:Redmi K30 Pro};{yw_code:}",
    "Cookie": "",
    "Referer": "https://img.client.10010.com/jifenshangcheng/orderDetail?orderNo=DD202008071000299850000021056403&orderId=8a2989eb73c452f10173c6a5ee240d9e&from=955000006&pip="
}

# 邮箱信息
mail_host = 'smtp.163.com'
mail_user = 'minu_bot@163.com'
mail_pass = ''
sender = "minu_bot@163.com"
receivers = 'minured@qq.com'
title = "联通星期五 抢购详情"


def getGoods():
    url = "https://m.client.10010.com/welfare-mall-front-activity/mobile/activity/get619Activity/v1"

    payload = {
        "whetherFriday": "YES",
        "from": "955000006"
    }

    res = requests.get(url, params=payload, headers=headers).json()
    print(res)
    if (res["msg"] == "未登录"):
        print("未登录,请检查cookie")
    else:
        print("已获取物品列表:")
        goods = []
        for i in res["resdata"]["goodsList"]:
            print(i["gOODS_NAME"])
            goods.append(i["gOODS_SKU_ID"])
        return goods


def sendEmail(data):
    # content
    dataStr = ""
    for i in data:
        dataStr += (str(i) + "\n")
    content = dataStr
    print(content)

    # 定义信息
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = receivers
    message['Subject'] = title

    # 实例
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("发送成功")
    except smtplib.SMTPException as e:
        print(e)


def save(res):
    with open("./result.html", "w+") as f:
        f.write(res.text)

# 商品id 和 金额
def order(id, amount, tel):
    order_url = "https://m.client.10010.com/welfare-mall-front/mobile/api/bj2402/v1"
    order_payload = {
        "reqsn": "c2cb171e-3ee6-2b67-93c2-e08ce70980d1",
        "reqtime": str(int(time.time() * 1000)),
        "cliver": "",
        "reqdata": '{"goodsId":"' + id + '","payWay":"01","amount":"' + amount + '","reChangeNo":"' + tel + '","saleTypes":"C","points":0,"beginTime":1597370400000,"imei":"b552f37f6359484cb4f90d869a367150","sourceChannel":"955000006955000006","proFlag":"","scene":"","promoterCode":"","maxcash":""}'

    }
    order_res = requests.post(order_url, data=order_payload, headers=headers).json()
    print(order_res)
    return order_res['msg']


# goods = getGoods()

# 美团外卖红包
goodsID = {
'red30': '8a29ac8972a48dc10172bb4eebaf0ce7',
'red10': '8a29ac8972a48dc10172bb4b994e0cc5',
'red5': '8a29ac8a72a48dbe0172bb4885430d81',
'red3': '8a29ac8a72be05a70172c067722600b8'
}

print('开始定时任务： 联通星期五')

def test():
    print("定时器执行了")

def sendTips():
    msgUrl = 'https://sc.ftqq.com/SCU81312Tf5ae9b79b6237a4549b0c52edb9fb7a65e40043942ebb.send'
    payload = {
        'text': '请更新cookie，30分钟后开始抢购！'
    }
    res = requests.post(msgUrl, data=payload)
    print(res)

def placeOrder():
    i = 0
    result = []
    while (i < 15):
        result.append(order(goodsID['red30'], "10", "13226408930"))
        i += 1
        time.sleep(0.5)
    sendEmail(result)



schedule.every().friday.at("09:30").do(sendTips)
schedule.every().friday.at("09:59:59").do(placeOrder)

# 测试
schedule.every().day.at("09:32").do(placeOrder)

while True:
    schedule.run_pending()
    time.sleep(1)



# updateTime: 202000921

# cookieTime: 202009018



