import asyncio
import functools as ft


SQL_CREATE_TABLE = [
    '''
    CREATE TABLE people (
        id INTEGER PRIMARY KEY,
        name TEXT
    );
    ''',
]


def sync(method):
    @ft.wraps(method)
    def wrapper(self, *args, **kwargs):
        loop = asyncio.get_event_loop()
        f = method(self, *args, **kwargs)
        return loop.run_until_complete(f)
    return wrapper
