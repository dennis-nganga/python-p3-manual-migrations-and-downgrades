"""Renaming students to scholars

Revision ID: 96495bbe936d
Revises: 791279dd0760
Create Date: 2023-06-10 12:55:24.320572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96495bbe936d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')