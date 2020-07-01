import dataclasses

from flask import Blueprint
from flask_restful import Api, Resource

from services.todo import ToDoService, ToDoServiceSingleton

api_bp = Blueprint('api', __name__)

api = Api(api_bp)


class TodoList(Resource):
    todo_service = ToDoServiceSingleton

    def get(self):
        todos = self.todo_service.fetch_todos()

        # marshalling/serialization
        todo_dicts =[
            todo.as_jsonable_dict()
            for todo in todos
        ]

        return {
            'result': todo_dicts,
        }


class TodoItem(Resource):
    todo_service = ToDoServiceSingleton

    def get(self, id):
        todo = ToDoServiceSingleton.fetch_by_id(id)
        return {
            'result': todo.as_jsonable_dict()
        }


api.add_resource(TodoItem, '/todos/<string:id>')
api.add_resource(TodoList, '/todos')
