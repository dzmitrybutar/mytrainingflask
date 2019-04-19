"""add language to posts

Revision ID: 543e9b50dc8a
Revises: e58a4903cbbc
Create Date: 2019-04-19 03:16:23.707619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '543e9b50dc8a'
down_revision = 'e58a4903cbbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
