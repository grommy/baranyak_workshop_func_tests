import requests
from api_functional_tests.config import API_URL, TASKS_TAIL, TASK_TAIL
from api_functional_tests.config import DEFAULT_USERNAME as USERNAME
from api_functional_tests.config import DEFAULT_PASSWORD as PASSWORD
from api_functional_tests.core.task_parser import ResponseParser


class TaskHandler:
    @classmethod
    def get_task(cls, task_id, username, password):
        """

        :param username:
        :param password:
        :return:
        """

        raw_response = requests.get(url=API_URL+TASK_TAIL+str(task_id), auth=(username, password))
        return ResponseParser.get_task(raw_response)


if __name__ == '__main__':
    task_1 = TaskHandler.get_tasks(task_id=1,username=USERNAME, password=PASSWORD)
    print(task_1)
