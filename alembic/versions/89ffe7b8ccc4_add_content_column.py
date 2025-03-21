"""add content column

Revision ID: 89ffe7b8ccc4
Revises: ed2c03be4669
Create Date: 2024-12-16 15:30:50.603969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89ffe7b8ccc4'
down_revision: Union[str, None] = 'ed2c03be4669'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
