"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.change_type

ChangeTypeList: TypeAlias = list["aws_sdk_cleanrooms.types.change_type.ChangeType"]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeTypeList) -> list:
    import aws_sdk_cleanrooms.types.change_type

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.change_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeTypeList:
    import aws_sdk_cleanrooms.types.change_type

    out: ChangeTypeList = []
    for item in data:
        out.append(aws_sdk_cleanrooms.types.change_type.deserialize_json(item))
    return out
