"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#TagOnCreateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_video.types.tag

TagOnCreateList: TypeAlias = list["capo_kinesis_video.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: TagOnCreateList) -> list:
    import capo_kinesis_video.types.tag

    out: list = []
    for item in value:
        out.append(capo_kinesis_video.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagOnCreateList:
    import capo_kinesis_video.types.tag

    out: TagOnCreateList = []
    for item in data:
        out.append(capo_kinesis_video.types.tag.deserialize_json(item))
    return out
