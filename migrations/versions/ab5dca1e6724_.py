"""empty message

Revision ID: ab5dca1e6724
Revises: 
Create Date: 2023-11-16 19:14:04.723351

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ab5dca1e6724'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('form_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('form_data', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_form_data_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('form_data', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_form_data_id'))

    op.drop_table('form_data')
    # ### end Alembic commands ###