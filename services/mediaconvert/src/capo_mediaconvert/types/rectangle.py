"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Rectangle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max2147483647
    import capo_mediaconvert.types.__integer_min2_max2147483647


class Rectangle(TypedDict, closed=True):
    height: NotRequired[
        "capo_mediaconvert.types.__integer_min2_max2147483647.__integerMin2Max2147483647"
    ]
    """Height of rectangle in pixels. Specify only even numbers."""
    width: NotRequired[
        "capo_mediaconvert.types.__integer_min2_max2147483647.__integerMin2Max2147483647"
    ]
    """Width of rectangle in pixels. Specify only even numbers."""
    x: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """The distance, in pixels, between the rectangle and the left edge of the video frame. Specify only even numbers."""
    y: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """The distance, in pixels, between the rectangle and the top edge of the video frame. Specify only even numbers."""


# --- restJson1 ser/de ---
def serialize_json(value: Rectangle) -> dict:
    out: dict = {}
    if "height" in value:
        out["height"] = value["height"]
    if "width" in value:
        out["width"] = value["width"]
    if "x" in value:
        out["x"] = value["x"]
    if "y" in value:
        out["y"] = value["y"]
    return out


def deserialize_json(data: dict) -> Rectangle:
    out: Rectangle = {}  # type: ignore[typeddict-item]
    if "height" in data:
        out["height"] = data["height"]
    if "width" in data:
        out["width"] = data["width"]
    if "x" in data:
        out["x"] = data["x"]
    if "y" in data:
        out["y"] = data["y"]
    return out
