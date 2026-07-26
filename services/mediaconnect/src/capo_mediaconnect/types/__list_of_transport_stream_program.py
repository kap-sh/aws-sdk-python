"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfTransportStreamProgram``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.transport_stream_program

__listOfTransportStreamProgram: TypeAlias = list[
    "capo_mediaconnect.types.transport_stream_program.TransportStreamProgram"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTransportStreamProgram) -> list:
    import capo_mediaconnect.types.transport_stream_program

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.transport_stream_program.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfTransportStreamProgram:
    import capo_mediaconnect.types.transport_stream_program

    out: __listOfTransportStreamProgram = []
    for item in data:
        out.append(
            capo_mediaconnect.types.transport_stream_program.deserialize_json(item)
        )
    return out
