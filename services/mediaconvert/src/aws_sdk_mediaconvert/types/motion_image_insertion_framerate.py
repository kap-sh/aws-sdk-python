"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MotionImageInsertionFramerate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min1_max17895697
    import aws_sdk_mediaconvert.types.__integer_min1_max2147483640


class MotionImageInsertionFramerate(TypedDict, closed=True):
    framerate_denominator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max17895697.__integerMin1Max17895697"
    ]
    """The bottom of the fraction that expresses your overlay frame rate. For example, if your frame rate is 24 fps, set this value to 1."""
    framerate_numerator: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max2147483640.__integerMin1Max2147483640"
    ]
    """The top of the fraction that expresses your overlay frame rate. For example, if your frame rate is 24 fps, set this value to 24."""


# --- restJson1 ser/de ---
def serialize_json(value: MotionImageInsertionFramerate) -> dict:
    out: dict = {}
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    return out


def deserialize_json(data: dict) -> MotionImageInsertionFramerate:
    out: MotionImageInsertionFramerate = {}  # type: ignore[typeddict-item]
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    return out
