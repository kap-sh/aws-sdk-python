"""Generated from Smithy shape ``com.amazonaws.iot#ActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.action

ActionList: TypeAlias = list["aws_sdk_iot.types.action.Action"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionList) -> list:
    import aws_sdk_iot.types.action

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionList:
    import aws_sdk_iot.types.action

    out: ActionList = []
    for item in data:
        out.append(aws_sdk_iot.types.action.deserialize_json(item))
    return out
