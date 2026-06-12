"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionSourceFramerate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max1001
    import aws_sdk_mediaconvert.types.__integer_min1_max60000


class CaptionSourceFramerate(TypedDict):
    framerate_denominator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max1001.__integerMin1Max1001"
    ]
    """Specify the denominator of the fraction that represents the frame rate for the setting Caption source frame rate. Use this setting along with the setting Framerate numerator."""
    framerate_numerator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max60000.__integerMin1Max60000"
    ]
    """Specify the numerator of the fraction that represents the frame rate for the setting Caption source frame rate. Use this setting along with the setting Framerate denominator."""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSourceFramerate) -> dict:
    out: dict = {}
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    return out


def deserialize_json(data: dict) -> CaptionSourceFramerate:
    out: CaptionSourceFramerate = {}  # type: ignore[typeddict-item]
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    return out
