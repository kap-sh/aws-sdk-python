"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.group

GroupList: TypeAlias = list["aws_sdk_quicksight.types.group.Group"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupList) -> list:
    import aws_sdk_quicksight.types.group

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.group.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupList:
    import aws_sdk_quicksight.types.group

    out: GroupList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.group.deserialize_json(item))
    return out
