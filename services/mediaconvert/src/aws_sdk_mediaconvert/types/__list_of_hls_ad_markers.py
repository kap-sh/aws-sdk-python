"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfHlsAdMarkers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.hls_ad_markers

__listOfHlsAdMarkers: TypeAlias = list[
    "aws_sdk_mediaconvert.types.hls_ad_markers.HlsAdMarkers"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfHlsAdMarkers) -> list:
    import aws_sdk_mediaconvert.types.hls_ad_markers

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.hls_ad_markers.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfHlsAdMarkers:
    import aws_sdk_mediaconvert.types.hls_ad_markers

    out: __listOfHlsAdMarkers = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.hls_ad_markers.deserialize_json(item))
    return out
