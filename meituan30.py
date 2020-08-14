import requests
import time

tencent = "8a29ac8a73a10a640173c7fa389f0a7a"
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi K30 Pro Build/QKQ1.200419.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36; unicom{version:android@7.0400,desmobile:13226408930};devicetype{deviceBrand:Xiaomi,deviceModel:Redmi K30 Pro};{yw_code:}",
    "Cookie": "MUT_S=android10; a_token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTc5NDcyMTksInRva2VuIjp7ImxvZ2luVXNlciI6IjEzMjI2NDA4OTMwIiwicmFuZG9tU3RyIjoieWhlMTU0ZTUxNTk3MzQyNDE5In0sImlhdCI6MTU5NzM0MjQxOX0.AvAtVcmRCPlzunH3gFlbJ3DQHySEWZ96fDgHCJDrrGpWuyaNfhBHyoqMYxEhXXEj_b6FMBrO06p1MB8HGSl18Q; c_id=670346726278139c691714cb20382115232f05f28a970f4c70a2c7b09acebf11; login_type=01; login_type=01; u_account=13226408930; city=051|510|90472586|-99; c_version=android@7.0400; d_deviceCode=b552f37f6359484cb4f90d869a367150; enc_acc=Z1asKO8D/qJlatrNoegRMc31p6rleB9dWQuj6Sf/DVmULsKCHJ2hmdezQJrg9hh00hD2xZVkWo7T6tUh27SZ2mB9BipCcyCvO+swqpyzwV518H/lpRQmEe6yh2UB3KdqDuIZT4P5JnWLcAMeYaqMg7YibUlWsUZ69f55C9jvGBI=; ecs_acc=Z1asKO8D/qJlatrNoegRMc31p6rleB9dWQuj6Sf/DVmULsKCHJ2hmdezQJrg9hh00hD2xZVkWo7T6tUh27SZ2mB9BipCcyCvO+swqpyzwV518H/lpRQmEe6yh2UB3KdqDuIZT4P5JnWLcAMeYaqMg7YibUlWsUZ69f55C9jvGBI=; random_login=0; cw_mutual=6ff66a046d4cb9a67af6f2af5f74c321d27b08ed87027ce200247d1aa4e574cbd3239d0813f610d8ed628d3502a3ad2f2bad4eb5711fc11a833428dcb9b8a3dd; t3_token=7d1990b1ebfe2d4870a5d966ba377c4f; invalid_at=36663909dc5d99b29c4a78e937f93c2847536050d67e6a28962e5f508bad7692; c_mobile=13226408930; wo_family=0; u_areaCode=510; third_token=eyJkYXRhIjoiMTMyYzJlNGFmOTFiOWU0ZTRmMmMyMDQwOWVkNWU5NDI2MjhhYzNjOWI0YTRlZTlmMjVmZDkzZjFhNDgyZDA3ZDU1MTFkZmE0YTBkODQ2ODI2MzY5ZTUzNzQ1OWNjZTdjNGUzYzFlMjAzNzVkNzVlYjQ4MmNjMzExMGVjMmMwZjJiNDFkOTMyNDAxZDE5NTA1YTE4ZTkwZGE3YWQ3YWUwZSIsInZlcnNpb24iOiIwMCJ9; ecs_token=eyJkYXRhIjoiNWVjMzc1MzNjZDhiYmJhZTEwYWQ1NDMzYjIyNDJkODc1YThhMjBiZmJjYWIwZDNhOTI4NTNkYTcwODBmZGRlYjNlYjM1MDUwYjVjNGVkMWM0OWY0YzMyZjU2YjcwODUyZWM3MTUxMThmOTcxN2M5YmQ1ZTNjYzY2MGIzZDU2Y2FmYzRmYTgxYTIxMTExMjIwMmNlZTZmYjM0MWIyZWZiOTE2YTc5YTdlMWIzZTkzYjU4ZDA0YjY4OWRlNTIxNzA2IiwidmVyc2lvbiI6IjAwIn0=; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxMzIyNjQwODkzMCIsInBybyI6IjA1MSIsImNpdHkiOiI1MTAiLCJpZCI6Ijc5ZDA2MjM2ZWM0MGY3ZTg0NjI3NjNlZDdkY2MxMWE3In0.SZgY4MTINP-vtxr3zUqmQrtb5DT7edVnGF-ADxGf9Xw; c_sfbm=234g_00; ecs_acc=Z1asKO8D/qJlatrNoegRMc31p6rleB9dWQuj6Sf/DVmULsKCHJ2hmdezQJrg9hh00hD2xZVkWo7T6tUh27SZ2mB9BipCcyCvO+swqpyzwV518H/lpRQmEe6yh2UB3KdqDuIZT4P5JnWLcAMeYaqMg7YibUlWsUZ69f55C9jvGBI=; mobileServiceAll=699fd00ce795990ed800b25eee61bc88; mobileService1=LMbpBwncBl6z3wk0Bh0aYNAx0D65E2V-H4ofoGom3hnh8RpP892G!982358339; logHostIP=null; c_sfbm=234g_00; on_info=6e287cc855950ad0751dbd7f4ae6ffa1; mobileServiceAll=504c96ee1af177f3b537134fed1e9564; mobileService1=FZ_pBwo5FXYL5B8RBUg8ZUyOHji0QL9_-guj0FPEFuRCwMbx5hN8!1401927444; ecs_acc=Z1asKO8D/qJlatrNoegRMc31p6rleB9dWQuj6Sf/DVmULsKCHJ2hmdezQJrg9hh00hD2xZVkWo7T6tUh27SZ2mB9BipCcyCvO+swqpyzwV518H/lpRQmEe6yh2UB3KdqDuIZT4P5JnWLcAMeYaqMg7YibUlWsUZ69f55C9jvGBI=; logHostIP=null; importantroute=1597342423.187.151095.324944; JSESSIONID=138B33171804888BA5F9DFFF618477F4; route=4409263098d857a3cc010d262182161c",
    "Referer": "https://img.client.10010.com/jifenshangcheng/orderDetail?orderNo=DD202008071000299850000021056403&orderId=8a2989eb73c452f10173c6a5ee240d9e&from=955000006&pip="
}
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
        print ("已获取物品列表:")
        goods = []
        for i in res["resdata"]["goodsList"]:
            print(i["gOODS_NAME"])
            goods.append(i["gOODS_SKU_ID"])
        return goods

def save(res):
    with open("./result.html", "w+") as f:
        f.write(res.text)

def order(id, amount):
    order_url = "https://m.client.10010.com/welfare-mall-front/mobile/api/bj2402/v1"

    order_payload = {
    "reqsn": "c2cb171e-3ee6-2b67-93c2-e08ce70980d1",
    # 下单时间-需要生成
    "reqtime": str(int(time.time()*1000)),
    # "reqtime": "1597375380333",

    "cliver": "",
    # 物品ID-自行选择
    "reqdata": '{"goodsId":"'+id+'","payWay":"01","amount":"'+amount+'","saleTypes":"C","points":0,"beginTime":1597370400000,"imei":"b552f37f6359484cb4f90d869a367150","sourceChannel":"955000006955000006","proFlag":"","scene":"","promoterCode":"","maxcash":""}'
    }
    order_res = requests.post(order_url, data=order_payload, headers=headers).json()
    print(order_res['msg'])
    return order_res

goods = getGoods()
order_res = order(goods[0], "10")


