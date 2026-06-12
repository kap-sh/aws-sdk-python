"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfVideoOverlay``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.video_overlay

__listOfVideoOverlay: TypeAlias = list[
    "aws_sdk_mediaconvert.types.video_overlay.VideoOverlay"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVideoOverlay) -> list:
    import aws_sdk_mediaconvert.types.video_overlay

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.video_overlay.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfVideoOverlay:
    import aws_sdk_mediaconvert.types.video_overlay

    out: __listOfVideoOverlay = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.video_overlay.deserialize_json(item))
    return out
