"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfRtmpAdMarkers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.rtmp_ad_markers

__listOfRtmpAdMarkers: TypeAlias = list[
    "aws_sdk_medialive.types.rtmp_ad_markers.RtmpAdMarkers"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRtmpAdMarkers) -> list:
    import aws_sdk_medialive.types.rtmp_ad_markers

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.rtmp_ad_markers.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRtmpAdMarkers:
    import aws_sdk_medialive.types.rtmp_ad_markers

    out: __listOfRtmpAdMarkers = []
    for item in data:
        out.append(aws_sdk_medialive.types.rtmp_ad_markers.deserialize_json(item))
    return out
