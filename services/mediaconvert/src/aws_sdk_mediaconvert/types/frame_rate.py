"""Generated from Smithy shape ``com.amazonaws.mediaconvert#FrameRate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer


class FrameRate(TypedDict, closed=True):
    denominator: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The denominator, or bottom number, in the fractional frame rate. For example, if your frame rate is 24000 / 1001 (23.976 frames per second), then the denominator would be 1001."""
    numerator: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """The numerator, or top number, in the fractional frame rate. For example, if your frame rate is 24000 / 1001 (23.976 frames per second), then the numerator would be 24000."""


# --- restJson1 ser/de ---
def serialize_json(value: FrameRate) -> dict:
    out: dict = {}
    if "denominator" in value:
        out["denominator"] = value["denominator"]
    if "numerator" in value:
        out["numerator"] = value["numerator"]
    return out


def deserialize_json(data: dict) -> FrameRate:
    out: FrameRate = {}  # type: ignore[typeddict-item]
    if "denominator" in data:
        out["denominator"] = data["denominator"]
    if "numerator" in data:
        out["numerator"] = data["numerator"]
    return out
