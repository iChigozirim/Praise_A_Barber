"""empty message

Revision ID: 6aad87abdd83
Revises: cf31f8389860
Create Date: 2022-05-29 19:35:49.799613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aad87abdd83'
down_revision = 'cf31f8389860'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('style', sa.Column('ids', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('style', 'ids')
    # ### end Alembic commands ###