"""Generated from Smithy shape ``com.amazonaws.iot#ActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.action

ActionList: TypeAlias = list["capo_iot.types.action.Action"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionList) -> list:
    import capo_iot.types.action

    out: list = []
    for item in value:
        out.append(capo_iot.types.action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionList:
    import capo_iot.types.action

    out: ActionList = []
    for item in data:
        out.append(capo_iot.types.action.deserialize_json(item))
    return out
