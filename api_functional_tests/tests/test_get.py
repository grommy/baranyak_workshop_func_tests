import pytest
from api_functional_tests.core.task_handler import TaskHandler
from api_functional_tests.config import DEFAULT_USERNAME as USERNAME
from api_functional_tests.config import DEFAULT_PASSWORD as PASSWORD

def parametrize_task_id():
    return pytest.mark.parametrize("task_id,expected_title",
                                   [(1, 'Buy groceries'),
                                    (2, 'Learn Python'),
                                    (3, 'Learn Java8')],
                                   ids=['First','Second','Third'])



class TestGetMethod:

    @classmethod
    def setup_class(cls):
        cls.task_handler = TaskHandler

    @parametrize_task_id()
    def test_get_task(self, task_id, expected_title):
        actual_task = self.task_handler.get_task(task_id=task_id,
                                                 username=USERNAME,
                                                 password=PASSWORD)
        assert actual_task.title == expected_title

if __name__ == '__main__':
    pytest.main([__file__, ''])

