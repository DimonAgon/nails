
import sqlalchemy as sqlAl
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped


class Base(DeclarativeBase): pass

class Entry(Base):
    __tablename__ = "entries"

    id: Mapped[int] = sqlAl.orm.mapped_column(sqlAl.Integer, primary_key=True)

    date: Mapped[str] = sqlAl.orm.mapped_column(sqlAl.VARCHAR(10))

    time: Mapped[int] = sqlAl.orm.mapped_column(sqlAl.VARCHAR(5))

    name: Mapped[str] = sqlAl.orm.mapped_column(sqlAl.VARCHAR(50))


