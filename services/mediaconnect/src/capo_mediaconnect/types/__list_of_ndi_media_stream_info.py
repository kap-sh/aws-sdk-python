"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfNdiMediaStreamInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.ndi_media_stream_info

__listOfNdiMediaStreamInfo: TypeAlias = list[
    "capo_mediaconnect.types.ndi_media_stream_info.NdiMediaStreamInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfNdiMediaStreamInfo) -> list:
    import capo_mediaconnect.types.ndi_media_stream_info

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.ndi_media_stream_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfNdiMediaStreamInfo:
    import capo_mediaconnect.types.ndi_media_stream_info

    out: __listOfNdiMediaStreamInfo = []
    for item in data:
        out.append(capo_mediaconnect.types.ndi_media_stream_info.deserialize_json(item))
    return out
