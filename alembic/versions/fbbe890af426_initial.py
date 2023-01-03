"""initial

Revision ID: fbbe890af426
Revises: 
Create Date: 2023-01-01 12:40:34.233650

"""
from alembic import op
import sqlalchemy as sa
import clickhouse_sqlalchemy
from clickhouse_sqlalchemy import engines

# revision identifiers, used by Alembic.
revision = "fbbe890af426"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "events",
        sa.Column(
            "created_at", clickhouse_sqlalchemy.types.common.DateTime64(), nullable=False
        ),
        sa.Column("user_id", clickhouse_sqlalchemy.types.common.Int(), nullable=True),
        sa.Column(
            "event_type", clickhouse_sqlalchemy.types.common.String(), nullable=False
        ),
        sa.PrimaryKeyConstraint("created_at"),
        engines.MergeTree(
            partition_by=("created_at",),
            order_by=("created_at",),
            primary_key=("created_at",),
        ),)


def downgrade():
    op.drop_table("events")
