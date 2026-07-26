"""Generated from Smithy shape ``com.amazonaws.backup#CopyActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.copy_action

CopyActions: TypeAlias = list["capo_backup.types.copy_action.CopyAction"]


# --- restJson1 ser/de ---
def serialize_json(value: CopyActions) -> list:
    import capo_backup.types.copy_action

    out: list = []
    for item in value:
        out.append(capo_backup.types.copy_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> CopyActions:
    import capo_backup.types.copy_action

    out: CopyActions = []
    for item in data:
        out.append(capo_backup.types.copy_action.deserialize_json(item))
    return out
