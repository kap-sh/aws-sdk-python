"""Generated from Smithy shape ``com.amazonaws.dlm#ActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.action

ActionList: TypeAlias = list["aws_sdk_dlm.types.action.Action"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionList) -> list:
    import aws_sdk_dlm.types.action

    out: list = []
    for item in value:
        out.append(aws_sdk_dlm.types.action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionList:
    import aws_sdk_dlm.types.action

    out: ActionList = []
    for item in data:
        out.append(aws_sdk_dlm.types.action.deserialize_json(item))
    return out
