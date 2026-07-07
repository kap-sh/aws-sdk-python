"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MotionImageInsertionOffset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647


class MotionImageInsertionOffset(TypedDict, closed=True):
    image_x: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Set the distance, in pixels, between the overlay and the left edge of the video frame."""
    image_y: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Set the distance, in pixels, between the overlay and the top edge of the video frame."""


# --- restJson1 ser/de ---
def serialize_json(value: MotionImageInsertionOffset) -> dict:
    out: dict = {}
    if "image_x" in value:
        out["imageX"] = value["image_x"]
    if "image_y" in value:
        out["imageY"] = value["image_y"]
    return out


def deserialize_json(data: dict) -> MotionImageInsertionOffset:
    out: MotionImageInsertionOffset = {}  # type: ignore[typeddict-item]
    if "imageX" in data:
        out["image_x"] = data["imageX"]
    if "imageY" in data:
        out["image_y"] = data["imageY"]
    return out
