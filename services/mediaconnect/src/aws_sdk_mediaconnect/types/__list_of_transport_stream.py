"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfTransportStream``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.transport_stream

__listOfTransportStream: TypeAlias = list[
    "aws_sdk_mediaconnect.types.transport_stream.TransportStream"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTransportStream) -> list:
    import aws_sdk_mediaconnect.types.transport_stream

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.transport_stream.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTransportStream:
    import aws_sdk_mediaconnect.types.transport_stream

    out: __listOfTransportStream = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.transport_stream.deserialize_json(item))
    return out
