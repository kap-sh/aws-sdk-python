"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfNdiSourceInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.ndi_source_info

__listOfNdiSourceInfo: TypeAlias = list[
    "capo_mediaconnect.types.ndi_source_info.NdiSourceInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfNdiSourceInfo) -> list:
    import capo_mediaconnect.types.ndi_source_info

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.ndi_source_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfNdiSourceInfo:
    import capo_mediaconnect.types.ndi_source_info

    out: __listOfNdiSourceInfo = []
    for item in data:
        out.append(capo_mediaconnect.types.ndi_source_info.deserialize_json(item))
    return out
