"""initial migration

Revision ID: 7449b6de3ef9
Revises: 
Create Date: 2023-12-11 17:50:48.574419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7449b6de3ef9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shared_file', schema=None) as batch_op:
        batch_op.add_column(sa.Column('salt', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shared_file', schema=None) as batch_op:
        batch_op.drop_column('salt')

    # ### end Alembic commands ###
