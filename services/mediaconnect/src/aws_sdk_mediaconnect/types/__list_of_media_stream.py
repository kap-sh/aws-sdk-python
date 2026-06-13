"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfMediaStream``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.media_stream

__listOfMediaStream: TypeAlias = list[
    "aws_sdk_mediaconnect.types.media_stream.MediaStream"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaStream) -> list:
    import aws_sdk_mediaconnect.types.media_stream

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.media_stream.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMediaStream:
    import aws_sdk_mediaconnect.types.media_stream

    out: __listOfMediaStream = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.media_stream.deserialize_json(item))
    return out
