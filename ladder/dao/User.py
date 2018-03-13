
import json

class User:
    def __init__(self):
        self.user_id = 0
        self.qq_no = ""
        self.qq_nicheng = ""
        self.wechat = ""
        self.xianyu = ""
        self.zhuanzhuan = ""
        self.real_name = ""
        self.phone_no = ""

    def insertUser(self,dataStr):
        data=json.loads(dataStr)
        print(data['user_id'])
        print(data['wechat'])


if __name__=='__main__':

    data = '{"user_id":"0001","qq_no":"123456"}'
    user=User()
    user.insertUser(data)