"""Generated from Smithy shape ``com.amazonaws.pipes#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.tag

TagList: TypeAlias = list["aws_sdk_pipes.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: TagList) -> list:
    import aws_sdk_pipes.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_pipes.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagList:
    import aws_sdk_pipes.types.tag

    out: TagList = []
    for item in data:
        out.append(aws_sdk_pipes.types.tag.deserialize_json(item))
    return out
