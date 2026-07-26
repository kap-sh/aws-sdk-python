"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfQueue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.queue

__listOfQueue: TypeAlias = list["capo_mediaconvert.types.queue.Queue"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfQueue) -> list:
    import capo_mediaconvert.types.queue

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.queue.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfQueue:
    import capo_mediaconvert.types.queue

    out: __listOfQueue = []
    for item in data:
        out.append(capo_mediaconvert.types.queue.deserialize_json(item))
    return out
