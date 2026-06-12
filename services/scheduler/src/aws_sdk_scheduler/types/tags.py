"""Generated from Smithy shape ``com.amazonaws.scheduler#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.tag_map

Tags: TypeAlias = list["aws_sdk_scheduler.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: Tags) -> list:
    import aws_sdk_scheduler.types.tag_map

    out: list = []
    for item in value:
        out.append(aws_sdk_scheduler.types.tag_map.serialize_json(item))
    return out


def deserialize_json(data: list) -> Tags:
    import aws_sdk_scheduler.types.tag_map

    out: Tags = []
    for item in data:
        out.append(aws_sdk_scheduler.types.tag_map.deserialize_json(item))
    return out
