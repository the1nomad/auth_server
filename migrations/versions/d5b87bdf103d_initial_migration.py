"""Initial migration.

Revision ID: d5b87bdf103d
Revises: ea57a542b328
Create Date: 2022-03-02 15:21:18.220985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5b87bdf103d'
down_revision = 'ea57a542b328'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('firstname', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'firstname')
    # ### end Alembic commands ###