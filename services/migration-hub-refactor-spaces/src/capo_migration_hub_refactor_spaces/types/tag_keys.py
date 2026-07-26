"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#TagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.string

TagKeys: TypeAlias = list["capo_migration_hub_refactor_spaces.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeys:
    return list(data)
