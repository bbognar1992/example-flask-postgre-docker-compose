"""create my table

Revision ID: b484b0b95308
Revises: 
Create Date: 2020-05-29 10:34:26.368241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b484b0b95308'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'my_table',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column('ts_created', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('r_value', sa.Integer(), nullable=False)
    )


def downgrade():
    op.drop_table('my_table')
