"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfAddMediaStreamRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.add_media_stream_request

__listOfAddMediaStreamRequest: TypeAlias = list[
    "capo_mediaconnect.types.add_media_stream_request.AddMediaStreamRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAddMediaStreamRequest) -> list:
    import capo_mediaconnect.types.add_media_stream_request

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.add_media_stream_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfAddMediaStreamRequest:
    import capo_mediaconnect.types.add_media_stream_request

    out: __listOfAddMediaStreamRequest = []
    for item in data:
        out.append(
            capo_mediaconnect.types.add_media_stream_request.deserialize_json(item)
        )
    return out
