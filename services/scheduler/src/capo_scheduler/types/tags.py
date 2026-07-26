"""Generated from Smithy shape ``com.amazonaws.scheduler#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_scheduler.types.tag_map

Tags: TypeAlias = list["capo_scheduler.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: Tags) -> list:
    import capo_scheduler.types.tag_map

    out: list = []
    for item in value:
        out.append(capo_scheduler.types.tag_map.serialize_json(item))
    return out


def deserialize_json(data: list) -> Tags:
    import capo_scheduler.types.tag_map

    out: Tags = []
    for item in data:
        out.append(capo_scheduler.types.tag_map.deserialize_json(item))
    return out
