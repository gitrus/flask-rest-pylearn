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

