from sqlalchemy import Column
from clickhouse_sqlalchemy import types, engines
from db.base_class import Base


class Event(Base):

    id = Column(types.Int, primary_key=True, autoincrement=True)
    created_at = Column(types.DateTime, nullable=False)
    user_id = Column(types.Int, nullable=True)
    event_type = Column(types.String, nullable=False)

    order_by = ("created_at",)

    __table_args__ = (
        engines.MergeTree(
            order_by=order_by,
            partition_by=created_at,
        ),
    )

    __tablename__ = "events"
