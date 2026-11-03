"""Add indexes for channel message and reaction lookups."""

from alembic import op

revision = 'c4d7a9e215b8'
down_revision = 'e42c8f710a36'
branch_labels = None
depends_on = None

INDEXES = [
    ('ix_message_channel_parent_created', 'message', ['channel_id', 'parent_id', 'created_at']),
    ('ix_message_parent_id', 'message', ['parent_id']),
    ('ix_message_reaction_message_id', 'message_reaction', ['message_id']),
]


def upgrade() -> None:
    for name, table, columns in INDEXES:
        op.create_index(name, table, columns, if_not_exists=True)


def downgrade() -> None:
    for name, table, _ in INDEXES:
        op.drop_index(name, table_name=table, if_exists=True)
