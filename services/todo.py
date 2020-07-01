import datetime
import typing as t

from models.todo.todo import ToDo, ToDoStatus


class ToDoService:
    def update(self, todo: ToDo, update_obj: dict) -> ToDo:
        pass

    def create(self, create_obj: dict) -> ToDo:
        pass

    def fetch_overdue_todos(self, date: datetime) -> t.List[ToDo]:
        pass

    def complete_todo(self, todo: ToDo) -> ToDo:
        todo.status = ToDoStatus.DONE

        return todo

    def fetch_todos(self) -> t.List[ToDo]:
        return [
            ToDo('first', 'desc first'),
            ToDo('second', 'desc second')
        ]

    def fetch_by_id(self, uid: str) -> ToDo:
        return ToDo(
            uid,
            uid
        )


ToDoServiceSingleton = ToDoService()

"""
Rest API -> Adapter -> App logic (Service) -> Adapter db -> db
                            |
                           model

"""
