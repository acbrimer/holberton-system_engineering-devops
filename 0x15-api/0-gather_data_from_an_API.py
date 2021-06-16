#!/usr/bin/python3
"""
    Module 0-gather_data_from_an_API
"""
import sys
import requests

BASE_URI = 'https://jsonplaceholder.typicode.com/'

def get_user(user_id):
    """
        Fetches user info
        Request URI: https://jsonplaceholder.typicode.com/users/<user_id>
    """
    response = requests.get("{}users/{}".format(BASE_URI, user_id))
    return response.json()

def get_user_todos(user_id):
    """ 
        Fetches and prints todos for employee (user)
        Request URI: https://jsonplaceholder.typicode.com/todos?userId=<user_id>
    """
    response = requests.get("{}todos".format(BASE_URI), 
            params={ "userId": user_id })
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

if __name__ == '__main__':
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        list_user_todos(user_id)
