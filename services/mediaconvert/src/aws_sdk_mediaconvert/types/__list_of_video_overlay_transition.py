"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfVideoOverlayTransition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.video_overlay_transition

__listOfVideoOverlayTransition: TypeAlias = list[
    "aws_sdk_mediaconvert.types.video_overlay_transition.VideoOverlayTransition"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfVideoOverlayTransition) -> list:
    import aws_sdk_mediaconvert.types.video_overlay_transition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconvert.types.video_overlay_transition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfVideoOverlayTransition:
    import aws_sdk_mediaconvert.types.video_overlay_transition

    out: __listOfVideoOverlayTransition = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.video_overlay_transition.deserialize_json(item)
        )
    return out
