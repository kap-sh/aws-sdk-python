"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateTagValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.tag_value

UpdateTagValues: TypeAlias = list["aws_sdk_devops_guru.types.tag_value.TagValue"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTagValues) -> list:
    return list(value)


def deserialize_json(data: list) -> UpdateTagValues:
    return list(data)
