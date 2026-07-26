"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfMediaStream``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.media_stream

__listOfMediaStream: TypeAlias = list[
    "capo_mediaconnect.types.media_stream.MediaStream"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaStream) -> list:
    import capo_mediaconnect.types.media_stream

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.media_stream.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMediaStream:
    import capo_mediaconnect.types.media_stream

    out: __listOfMediaStream = []
    for item in data:
        out.append(capo_mediaconnect.types.media_stream.deserialize_json(item))
    return out
