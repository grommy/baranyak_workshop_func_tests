"""

"""
import json


class Task:
    """ This class models for tasks from TASK API """

    def __init__(self, title, description, task_id=None, status=False, uri=None):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.uri = uri

    def __str__(self):
        return json.dumps(self.__dict__)

    def __eq__(self, other):
        return self.title == other.title and \
                self.description == other.description


if __name__ == '__main__':
    task_1 = Task(title='new_title', description='new description', status=True)
    task_2 = Task(title='new_title', description='new description')
    print(task_1 is task_2)
    print(task_1 == task_2)
    print(task_1)

"""
        'id': 3,
        'title': 'Learn Java8',
        'description': 'Need to find a good Java tutorial on the web',
        'status': 'False'
"""
