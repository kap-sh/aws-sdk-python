"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.change

ChangeList: TypeAlias = list["aws_sdk_cleanrooms.types.change.Change"]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeList) -> list:
    import aws_sdk_cleanrooms.types.change

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.change.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeList:
    import aws_sdk_cleanrooms.types.change

    out: ChangeList = []
    for item in data:
        out.append(aws_sdk_cleanrooms.types.change.deserialize_json(item))
    return out
