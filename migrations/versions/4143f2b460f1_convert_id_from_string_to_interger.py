"""Convert id from string to interger

Revision ID: 4143f2b460f1
Revises: 4f6885a6400e
Create Date: 2022-05-23 13:48:08.450521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4143f2b460f1'
down_revision = '4f6885a6400e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('barber', sa.Column('phone', sa.String(length=80), nullable=True))
    op.add_column('barber', sa.Column('update_date', sa.DateTime(), nullable=True))
    op.create_unique_constraint(None, 'barber', ['phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'barber', type_='unique')
    op.drop_column('barber', 'update_date')
    op.drop_column('barber', 'phone')
    # ### end Alembic commands ###
