"""add retrait_depot_ok to user

Revision ID: 59879ea1b71c
Revises: 45d2e9717c18
Create Date: 2025-12-20 23:21:08.194303
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59879ea1b71c'
down_revision = '45d2e9717c18'
branch_labels = None
depends_on = None


def upgrade():
    # 1️⃣ Ajouter la colonne avec une valeur par défaut (évite NULL)
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'retrait_depot_ok',
                sa.Boolean(),
                nullable=False,
                server_default=sa.false()
            )
        )

    # 2️⃣ Nettoyer le server_default après création
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column(
            'retrait_depot_ok',
            server_default=None
        )


def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('retrait_depot_ok')
