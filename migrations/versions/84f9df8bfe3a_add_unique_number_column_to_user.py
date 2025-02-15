"""Add unique_number column to User

Revision ID: 84f9df8bfe3a
Revises: 
Create Date: 2024-07-08 19:22:32.783987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84f9df8bfe3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('unique_number', sa.Integer(), nullable=False))
        batch_op.create_unique_constraint(None, ['unique_number'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('unique_number')

    # ### end Alembic commands ###
