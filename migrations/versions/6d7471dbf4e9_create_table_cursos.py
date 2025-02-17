"""Create Table Cursos

Revision ID: 6d7471dbf4e9
Revises: 
Create Date: 2024-09-05 15:56:24.955779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d7471dbf4e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cursos',
    sa.Column('id_curso', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('duracao_horas', sa.Integer(), nullable=True),
    sa.Column('custo', sa.Float(precision=10, asdecimal=2), nullable=True),
    sa.PrimaryKeyConstraint('id_curso')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cursos')
    # ### end Alembic commands ###
