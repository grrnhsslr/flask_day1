"""empty message

Revision ID: 70dfbad0d36d
Revises: 24c9bd4b567c
Create Date: 2024-03-28 14:20:20.067452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70dfbad0d36d'
down_revision = '24c9bd4b567c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###