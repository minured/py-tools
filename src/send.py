import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "minu_bot@163.com"  # 用户名
mail_pass = "GFCWHXISGQPRJPDW"  # 授权密码，非登录密码
sender = "minu_bot@163.com"  # 发件人邮箱(最好写全, 不然会失败)

content = "hello"
receivers = "minured@qq.com"
title = "测试邮件"

def sendEmail():
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = receivers
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

sendEmail()