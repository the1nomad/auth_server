"""test splitting model file

Revision ID: f64b3c57c00b
Revises: d5b87bdf103d
Create Date: 2022-03-02 15:34:20.256321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f64b3c57c00b'
down_revision = 'd5b87bdf103d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('firstname', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key'),
    sa.UniqueConstraint('username', name='user_username_key')
    )
    # ### end Alembic commands ###
