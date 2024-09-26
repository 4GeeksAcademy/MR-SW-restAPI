"""empty message

Revision ID: 04ac58ea38d1
Revises: a5cffa318ac2
Create Date: 2024-09-26 20:30:30.906471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04ac58ea38d1'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('birth_year', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=50), nullable=True),
    sa.Column('species', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('release_date', sa.String(length=20), nullable=True),
    sa.Column('director', sa.String(length=100), nullable=True),
    sa.Column('producer', sa.String(length=100), nullable=True),
    sa.Column('episode_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('climate', sa.String(length=50), nullable=True),
    sa.Column('terrain', sa.String(length=50), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=True),
    sa.Column('manufacturer', sa.String(length=100), nullable=True),
    sa.Column('crew', sa.Integer(), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('firstname', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('lastname', sa.String(), nullable=False))
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('lastname')
        batch_op.drop_column('firstname')
        batch_op.drop_column('username')

    op.drop_table('favorite')
    op.drop_table('vehicle')
    op.drop_table('planet')
    op.drop_table('movie')
    op.drop_table('character')
    # ### end Alembic commands ###
