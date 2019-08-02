from locust import TaskSet, task, HttpLocust
import queue
import json
class UserBehavior(TaskSet):
    @task
    def test_login(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0; SM-G9350 Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044409 Mobile Safari/537.36 PuhuiApp/27",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "X-Requested-With": "XMLHttpRequest"
            }

        try:
            data = self.locust.user_data_queue.get()
        except queue.Empty:
            print('account data run out, test ended')
            exit(0)
        print('login with mobile: {0}, password: {1}' .format(data['username'], data['password']))
        payload = {
            'mobile': data['username'],
            'password': data['password']
        }

        req= self.client.post('/authentication/login', data=json.dumps(payload),headers=header, verify=False)
        self.locust.user_data_queue.put_nowait(data)
        if req.status_code == 200:
            print("success")
        else:
            print("fails")
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    user_data_queue = queue.Queue()
    # for index in range(100):
    data = {
            "username": "13717967937" ,
            "password": "123abc" ,
            # "email": "test%04d@debugtalk.test" % index,
            # "phone": "186%08d" % index,
        }
    user_data_queue.put_nowait(data)
    min_wait = 1000
    max_wait = 3000
if __name__ == "__main__":
    import os
    os.system("locust -f D:\mypython\mylocust01\puhuiinterface\loginforhyq.py --host=http://118.178.117.4:8000")