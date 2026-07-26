"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfTransportStream``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.transport_stream

__listOfTransportStream: TypeAlias = list[
    "capo_mediaconnect.types.transport_stream.TransportStream"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTransportStream) -> list:
    import capo_mediaconnect.types.transport_stream

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.transport_stream.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTransportStream:
    import capo_mediaconnect.types.transport_stream

    out: __listOfTransportStream = []
    for item in data:
        out.append(capo_mediaconnect.types.transport_stream.deserialize_json(item))
    return out
