import schedule
import time
from selenium import webdriver
import requests, json
import time

class piao:




    browser=""



    def job(self):


        # options = webdriver.ChromeOptions()
        # # 添加无界面参数
        # options.add_argument('--headless')
        # browser = webdriver.Chrome(options=options)

        self.browser.get(
            'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%BD%99%E5%A7%9A%E5%8C%97,CTH&ts=%E9%BA%BB%E5%9F%8E%E5%8C%97,MBN&date=2021-10-01&flag=N,N,Y')

        time.sleep(3)
        self.browser.find_element_by_link_text("确认").click()
        time.sleep(3)
        table_data = self.browser.find_element_by_id("queryLeftTable").find_elements_by_tag_name("tr")
        arr_dt = []
        for p in table_data:
            arr_dt.append(p.text)
            print()
        arr_dt2 = []
        for d in arr_dt:
            arr_dt2.append(d.replace("\n", " ").split(" "))
        print(arr_dt2)
        shu = 0
        pao = 10
        sm = ""
        for msg in arr_dt2:
            if len(msg) > 1:

                if msg[9] != "候补" and msg[9] != "--":
                    print(msg[0] + "二等座有票")
                    sm = msg[0] + "二等座"
                    pao = shu
                #     break
                # if msg[8]!="候补" and msg[8]!="--":
                #
                #     print(msg[0]+"一等座有票")
                #     sm = msg[0] + "一等座"
                #     pao = shu
                #     break

                shu = shu + 1
        if pao != 10:
            self.browser.find_elements_by_link_text("预订")[pao].click()

            time.sleep(3)
            self.browser.find_element_by_link_text("账号登录").click()
            time.sleep(1)
            self.browser.find_element_by_id("J-userName").send_keys("")  # 账号
            time.sleep(3)
            self.browser.find_element_by_id("J-password").send_keys("")  # 密码
            time.sleep(5)
            self.browser.find_element_by_link_text("立即登录").click()
            time.sleep(2)
            self.browser.find_element_by_link_text("短信验证").click()
            time.sleep(2)
            self.browser.find_element_by_id("id_card").send_keys("6016")
            time.sleep(2)
            self.browser.find_element_by_link_text("获取验证码").click()
            import json
            import requests as go

            data21 = {
                "appToken": "AT_YDIAvge78ZFoeTHGb3eBoioipp5PiAm6",
                "content": "已检测到车票：" + sm,
                "summary": "请打开apk",  # 消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
                "contentType": 1,  # 内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown
                "topicIds": [  # 发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。

                ],
                "uids": [  # 发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
                    "UID_u13caxS0OsCRx9SXGdOhPI6zen2I"
                ],
                "url": "http://wcphp172.xinhaimobile.cn/cf/"  # 原文链接，可选参数
            }

            print(go.post("http://wxpusher.zjiecode.com/api/send/message", json=data21).text)
            time.sleep(60)
            # 打开apk应用
            # 等待验证码
            dd = json.loads(requests.get("http://port.wapjin.com/cat_msg?strAddress=12306").text)["data"]
            code = dd[len(dd) - 1:][0][1][
                   dd[len(dd) - 1:][0][1].find("验证码：") + 4:dd[len(dd) - 1:][0][1].find("验证码：") + 10]
            time.sleep(2)
            self.browser.find_element_by_id("code").send_keys(code)
            time.sleep(2)
            self.browser.find_element_by_link_text("确定").click()
            time.sleep(3)
            self.browser.find_element_by_id("djPassenger_0").click()
            time.sleep(3)
            self.browser.find_element_by_link_text("提交订单").click()
            time.sleep(3)
            self.browser.find_element_by_link_text("确认").click()
            print(arr_dt2)
            import json
            import requests as go

            data2 = {
                "appToken": "AT_YDIAvge78ZFoeTHGb3eBoioipp5PiAm6",
                "content": "已经抢到车票：" + sm,
                "summary": "已经抢到车票请在30分钟内付款",  # 消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
                "contentType": 1,  # 内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown
                "topicIds": [  # 发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。

                ],
                "uids": [  # 发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
                    "UID_u13caxS0OsCRx9SXGdOhPI6zen2I"
                ],
                "url": "http://wcphp172.xinhaimobile.cn/cf/"  # 原文链接，可选参数
            }

            print(go.post("http://wxpusher.zjiecode.com/api/send/message", json=data2).text)
            self.browser.quit()


    def ends(self):
        schedule.clear('daily-tasks')
        self.browser.quit()


    def strs(self):
        self.browser = webdriver.Chrome()
        schedule.every(10).seconds.do(self.job).tag('daily-tasks', 'friend')



    def piao(self):
        schedule.every().day.at("20:52").do(self.strs)
        schedule.every().day.at("20:53").do(self.ends)
        schedule.every().day.at("20:54").do(self.strs)

        while True:
            schedule.run_pending()
            time.sleep(1)

piao().piao()

    # browser.get('https://kyfw.12306.cn/otn/resources/login.html')


    # browser.find_element_by_link_text("确定").click()
    # time.sleep(2)
    # browser.find_element_by_link_text("首页").click()
    # time.sleep(2)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
