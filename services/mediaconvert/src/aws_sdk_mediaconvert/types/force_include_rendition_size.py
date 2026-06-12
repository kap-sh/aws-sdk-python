"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ForceIncludeRenditionSize``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min32_max8192


class ForceIncludeRenditionSize(TypedDict):
    height: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8192.__integerMin32Max8192"
    ]
    """Use Height to define the video resolution height, in pixels, for this rule."""
    width: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32_max8192.__integerMin32Max8192"
    ]
    """Use Width to define the video resolution width, in pixels, for this rule."""


# --- restJson1 ser/de ---
def serialize_json(value: ForceIncludeRenditionSize) -> dict:
    out: dict = {}
    if "height" in value:
        out["height"] = value["height"]
    if "width" in value:
        out["width"] = value["width"]
    return out


def deserialize_json(data: dict) -> ForceIncludeRenditionSize:
    out: ForceIncludeRenditionSize = {}  # type: ignore[typeddict-item]
    if "height" in data:
        out["height"] = data["height"]
    if "width" in data:
        out["width"] = data["width"]
    return out
