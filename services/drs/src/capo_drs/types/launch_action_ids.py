"""Generated from Smithy shape ``com.amazonaws.drs#LaunchActionIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.launch_action_id

LaunchActionIds: TypeAlias = list["capo_drs.types.launch_action_id.LaunchActionId"]


# --- restJson1 ser/de ---
def serialize_json(value: LaunchActionIds) -> list:
    return list(value)


def deserialize_json(data: list) -> LaunchActionIds:
    return list(data)
