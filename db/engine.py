

from sqlalchemy.ext.asyncio import create_async_engine


engine = create_async_engine('sqlite+aiosqlite:///manik.db', echo=True)