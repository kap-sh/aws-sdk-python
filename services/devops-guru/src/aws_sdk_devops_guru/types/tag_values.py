"""Generated from Smithy shape ``com.amazonaws.devopsguru#TagValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.tag_value

TagValues: TypeAlias = list["aws_sdk_devops_guru.types.tag_value.TagValue"]


# --- restJson1 ser/de ---
def serialize_json(value: TagValues) -> list:
    return list(value)


def deserialize_json(data: list) -> TagValues:
    return list(data)
