#!/usr/bin/python3
"""
    Module 2-export_to_JSON
"""
import csv
import json
import requests
import sys

BASE_URI = 'https://jsonplaceholder.typicode.com/'


def get_user(user_id):
    """
        Fetches user info
        URI: https://jsonplaceholder.typicode.com/users/<user_id>
    """
    response = requests.get("{}users/{}".format(BASE_URI, user_id))
    return response.json()


def get_user_todos(user_id):
    """
        Fetches todos for employee (user)
        URI: https://jsonplaceholder.typicode.com/todos?userId=<user_id>
    """
    response = requests.get("{}todos".format(BASE_URI),
                            params={"userId": user_id})
    return response.json()


def list_user_todos(user_id):
    """
        Calls get_user and get_user_todos, prints response data
    """
    user = get_user(user_id)
    user_todos = get_user_todos(user_id)
    total_todos = len(user_todos)
    complete_todos = list(
        filter(lambda t: t['completed'], user_todos))
    print('Employee {} is done with tasks({}/{}):'.format(
        user['name'],
        len(complete_todos),
        total_todos))
    print('\t', end=' ')
    print('\n\t '.join(map(lambda t: t['title'], complete_todos)))


def list_user_todos_csv(user_id):
    """
        Calls get_user and get_user_todos, prints response data
    """
    user = get_user(user_id)
    user_todos = get_user_todos(user_id)
    for todo in user_todos:
        todo.update({'username': user['username']})
        del(todo['id'])
    cols = ['userId', 'username', 'completed', 'title']
    with open('{}.csv'.format(user_id), 'w') as f:
        dict_writer = csv.DictWriter(f, cols, quoting=csv.QUOTE_ALL)
        dict_writer.writerows(user_todos)


def list_user_todos_json(user_id):
    """
        Calls get_user and get_user_todos, writes response json to file
    """
    user = get_user(user_id)
    user_todos = get_user_todos(user_id)
    for todo in user_todos:
        todo['task'] = todo.pop('title')
        todo.update({'username': user['username']})
        del(todo['id'])
        del(todo['userId'])
    with open('{}.json'.format(user_id), 'w') as f:
        json.dump({user_id: user_todos}, f)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        list_user_todos_json(user_id)
