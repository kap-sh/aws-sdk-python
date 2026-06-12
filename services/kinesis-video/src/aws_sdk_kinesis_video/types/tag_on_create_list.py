"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#TagOnCreateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.tag

TagOnCreateList: TypeAlias = list["aws_sdk_kinesis_video.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: TagOnCreateList) -> list:
    import aws_sdk_kinesis_video.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_kinesis_video.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagOnCreateList:
    import aws_sdk_kinesis_video.types.tag

    out: TagOnCreateList = []
    for item in data:
        out.append(aws_sdk_kinesis_video.types.tag.deserialize_json(item))
    return out
