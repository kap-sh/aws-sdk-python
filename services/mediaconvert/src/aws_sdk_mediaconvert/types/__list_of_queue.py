"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfQueue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.queue

__listOfQueue: TypeAlias = list["aws_sdk_mediaconvert.types.queue.Queue"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfQueue) -> list:
    import aws_sdk_mediaconvert.types.queue

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.queue.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfQueue:
    import aws_sdk_mediaconvert.types.queue

    out: __listOfQueue = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.queue.deserialize_json(item))
    return out
