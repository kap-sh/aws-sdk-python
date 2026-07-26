"""Generated from Smithy shape ``com.amazonaws.mgn#ActionIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.action_id

ActionIDs: TypeAlias = list["capo_mgn.types.action_id.ActionID"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> ActionIDs:
    return list(data)
