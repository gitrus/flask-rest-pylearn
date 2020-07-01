import typing as t
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class ToDoPriority(Enum):
    CRITICAL = 'critical'
    NORMAL = 'normal'
    MINOR = 'minor'


class ToDoStatus(Enum):
    NEW = 'new'
    DONE = 'done'


@dataclass
class ToDo:
    """
    model = (entity name + entity attributes)
    ToDo is the main model of the service.
    User can create todo.
    """
    title: str
    description: str
    due_date: t.Optional[datetime] = None
    priority: ToDoPriority = ToDoPriority.NORMAL
    status: ToDoStatus = ToDoStatus.NEW

    def as_jsonable_dict(self):
        todo_dict = {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'priority': self.priority.value,
            'status': self.status.value,
        }

        return todo_dict
