class ReadOnly(object):

    def __init__(self, db):
        self._db = db

    async def __aenter__(self):
        self._cursor = await self._db.cursor()
        return self._cursor

    async def __aexit__(self, exc_type, exc, tb):
        await self._cursor.close()


class ReadWrite(object):

    def __init__(self, db):
        self._db = db

    async def __aenter__(self):
        self._cursor = await self._db.cursor()
        return self._cursor

    async def __aexit__(self, exc_type, exc, tb):
        if exc_type is None:
            await self._db.commit()
        else:
            await self._db.rollback()
        await self._cursor.close()
