"""empty message

Revision ID: 7d370809c988
Revises: 1d3a897f4a54
Create Date: 2022-05-31 14:18:08.905674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d370809c988'
down_revision = '1d3a897f4a54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('looking_for_venue', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'looking_for_venue')
    op.drop_column('Venue', 'seeking_description')
    # ### end Alembic commands ###
