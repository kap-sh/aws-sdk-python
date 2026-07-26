"""Generated from Smithy shape ``com.amazonaws.backup#IndexActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.index_action

IndexActions: TypeAlias = list["capo_backup.types.index_action.IndexAction"]


# --- restJson1 ser/de ---
def serialize_json(value: IndexActions) -> list:
    import capo_backup.types.index_action

    out: list = []
    for item in value:
        out.append(capo_backup.types.index_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> IndexActions:
    import capo_backup.types.index_action

    out: IndexActions = []
    for item in data:
        out.append(capo_backup.types.index_action.deserialize_json(item))
    return out
