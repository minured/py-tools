import requests
import time
import schedule
import smtplib
from email.mime.text import MIMEText
from email.header import Header

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi K30 Pro Build/QKQ1.200419.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36; unicom{version:android@7.0400,desmobile:13226408930};devicetype{deviceBrand:Xiaomi,deviceModel:Redmi K30 Pro};{yw_code:}",
    "Cookie": "MUT_S=android10; login_type=01; u_account=13226408930; city=051|510|90472586|-99; clientid=98|0; BIGipServerPOOL_SJYYT2_KHDJTZY_80=218958346.16927.0000; zg_did=%7B%22did%22%3A%20%22174493938a11c0-0e6f5546a06e72-6d10275f-53c31-174493938a236c%22%7D; zg_a59132f133104d7ab2ae3427e4d17684=%7B%22sid%22%3A%201598956320935%2C%22updated%22%3A%201598956345514%2C%22info%22%3A%201598956320945%2C%22superProperty%22%3A%20%22%7B%5C%22st_timestamp%5C%22%3A%20%5C%2220200901183146%5C%22%2C%5C%22st_position%5C%22%3A%20%5C%22STWDQB001%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%2213226408930%22%7D; devicedId=b552f37f6359484cb4f90d869a367150; cw_mutual=6ff66a046d4cb9a67af6f2af5f74c32182d7341bbf9a6268b3bd12762d4142a905ef85cc2438c05ad4dd26082c1548cae9cc5a741b71875585cf69111fc2457d; ecs_acc=ZQI0zcIH1kH/XsiIlilNt/eomgB4akJqnoodZ5a9vCeaZch90mvo8OnxZ6hc+YX6qU07r6YdNcEv3ibiAB6fV/AC3bwHBdtSHc3jZLa8ERPSIlUgL6ao59LSNoyWIJsni69D3DQWKU9evSlfAEzFu7G4kTctrXinuhvHwrQgycY=; ecs_token=eyJkYXRhIjoiNWVjMzc1MzNjZDhiYmJhZTEwYWQ1NDMzYjIyNDJkODc1YThhMjBiZmJjYWIwZDNhOTI4NTNkYTcwODBmZGRlYmIyNTNlZjVjNmEyNzliMDlkNmIyZWM5MTM5NThhNTAxZTBkZWZmMDJjNjU0ZjIyN2IwYTQ3ZmIxMDdlMzg5ZTI3NjljZjAxNmQ5Njc5NjNhZDU3OGRlMDFiOTBlMGI4M2YyYjZhMTVjNGFmOGVlYmJhZGQzZmQ0ZDJmZGZhY2EzIiwidmVyc2lvbiI6IjAwIn0=; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxMzIyNjQwODkzMCIsInBybyI6IjA1MSIsImNpdHkiOiI1MTAiLCJpZCI6IjU4MWY2ZDQ3Zjc2MTdjYWE3MTc2OWE3OWZhYmE3NGVkIn0.PP7W1l8NvhDGEqzTMLbpbv5rjZf8PGXg6bvaay_WJgI; acw_tc=9dff1e1715997874408672251e55a0b26362f12ec1597b96029c194643; _pk_ref.1.183e=%5B%22%22%2C%22%22%2C1599787442%2C%22https%3A%2F%2Fst.gd10010.cn%2Factivity-pages%2Fgetcouponactivity%2Finside%2Fpages%2F%3Fcookie%3Djx565714439255144995%22%5D; _pk_id.1.183e=f88b811b3510d895.1597370574.16.1599787442.1599787442.; _pk_ses.1.183e=1",
    "Referer": "https://img.client.10010.com/jifenshangcheng/orderDetail?orderNo=DD202008071000299850000021056403&orderId=8a2989eb73c452f10173c6a5ee240d9e&from=955000006&pip="
}

# 邮箱信息
mail_host = 'smtp.163.com'
mail_user = 'minu_bot@163.com'
mail_pass = 'GFCWHXISGQPRJPDW'
sender = "minu_bot@163.com"
receivers = 'minured@qq.com'
title = "联通星期五 抢购详情"

# 固定商品id （30-30）
red30 = "8a29ac8972a48dc10172bb4eebaf0ce7"


def getGoods():
    url = "https://m.client.10010.com/welfare-mall-front-activity/mobile/activity/get619Activity/v1"

    payload = {
        "whetherFriday": "YES",
        "from": "955000006"
    }

    res = requests.get(url, params=payload, headers=headers).json()
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


def order(id, amount):
    order_url = "https://m.client.10010.com/welfare-mall-front/mobile/api/bj2402/v1"
    order_payload = {
        "reqsn": "c2cb171e-3ee6-2b67-93c2-e08ce70980d1",
        "reqtime": str(int(time.time() * 1000)),
        "cliver": "",
        "reqdata": '{"goodsId":"' + id + '","payWay":"01","amount":"' + amount + '","saleTypes":"C","points":0,"beginTime":1597370400000,"imei":"b552f37f6359484cb4f90d869a367150","sourceChannel":"955000006955000006","proFlag":"","scene":"","promoterCode":"","maxcash":""}'
    }
    order_res = requests.post(order_url, data=order_payload, headers=headers).json()
    print(order_res)
    return order_res['msg']


# goods = getGoods()

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
    while (i < 10):
        result.append(order(red30, "10"))
        i += 1
        time.sleep(0.5)
    sendEmail(result)



schedule.every().friday.at("09:30").do(sendTips)
schedule.every().friday.at("09:59:59").do(placeOrder)

while True:
    schedule.run_pending()
    time.sleep(1)

# updateTime: 202000914
# cookieTime: 202009011



