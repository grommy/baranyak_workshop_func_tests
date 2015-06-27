import requests
from api_functional_tests.config import API_URL, TASKS_TAIL, TASK_TAIL
from api_functional_tests.config import DEFAULT_USERNAME as USERNAME
from api_functional_tests.config import DEFAULT_PASSWORD as PASSWORD

class TaskHandler:
    @classmethod
    def get_tasks(cls, username, password):
        """

        :param username:
        :param password:
        :return:
        """

        r = requests.get(url=API_URL+TASKS_TAIL, auth=(username, password))
        print(r.status_code)
        print(r.text)

if __name__ == '__main__':
    TaskHandler.get_tasks(USERNAME, PASSWORD)
