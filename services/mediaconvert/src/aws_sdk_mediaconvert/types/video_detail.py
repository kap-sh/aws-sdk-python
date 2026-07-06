"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer


class VideoDetail(TypedDict, closed=True):
    height_in_px: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Height in pixels for the output"""
    width_in_px: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Width in pixels for the output"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoDetail) -> dict:
    out: dict = {}
    if "height_in_px" in value:
        out["heightInPx"] = value["height_in_px"]
    if "width_in_px" in value:
        out["widthInPx"] = value["width_in_px"]
    return out


def deserialize_json(data: dict) -> VideoDetail:
    out: VideoDetail = {}  # type: ignore[typeddict-item]
    if "heightInPx" in data:
        out["height_in_px"] = data["heightInPx"]
    if "widthInPx" in data:
        out["width_in_px"] = data["widthInPx"]
    return out
