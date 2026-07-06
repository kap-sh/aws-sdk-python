"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ClipLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max128
    import aws_sdk_mediaconvert.types.__integer_min90_max105
    import aws_sdk_mediaconvert.types.__integer_min920_max1023
    import aws_sdk_mediaconvert.types.__integer_min_negative5_max10


class ClipLimits(TypedDict, closed=True):
    maximum_rgb_tolerance: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min90_max105.__integerMin90Max105"
    ]
    """Specify the Maximum RGB color sample range tolerance for your output. MediaConvert corrects any YUV values that, when converted to RGB, would be outside the upper tolerance that you specify. Enter an integer from 90 to 105 as an offset percentage to the maximum possible value. Leave blank to use the default value 100. When you specify a value for Maximum RGB tolerance, you must set Sample range conversion to Limited range clip."""
    maximum_yuv: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min920_max1023.__integerMin920Max1023"
    ]
    """Specify the Maximum YUV color sample limit. MediaConvert conforms any pixels in your input above the value that you specify to typical limited range bounds. Enter an integer from 920 to 1023. Leave blank to use the default value 940. The value that you enter applies to 10-bit ranges. For 8-bit ranges, MediaConvert automatically scales this value down. When you specify a value for Maximum YUV, you must set Sample range conversion to Limited range clip."""
    minimum_rgb_tolerance: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative5_max10.__integerMinNegative5Max10"
    ]
    """Specify the Minimum RGB color sample range tolerance for your output. MediaConvert corrects any YUV values that, when converted to RGB, would be outside the lower tolerance that you specify. Enter an integer from -5 to 10 as an offset percentage to the minimum possible value. Leave blank to use the default value 0. When you specify a value for Minimum RGB tolerance, you must set Sample range conversion to Limited range clip."""
    minimum_yuv: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max128.__integerMin0Max128"
    ]
    """Specify the Minimum YUV color sample limit. MediaConvert conforms any pixels in your input below the value that you specify to typical limited range bounds. Enter an integer from 0 to 128. Leave blank to use the default value 64. The value that you enter applies to 10-bit ranges. For 8-bit ranges, MediaConvert automatically scales this value down. When you specify a value for Minumum YUV, you must set Sample range conversion to Limited range clip."""


# --- restJson1 ser/de ---
def serialize_json(value: ClipLimits) -> dict:
    out: dict = {}
    if "maximum_rgb_tolerance" in value:
        out["maximumRGBTolerance"] = value["maximum_rgb_tolerance"]
    if "maximum_yuv" in value:
        out["maximumYUV"] = value["maximum_yuv"]
    if "minimum_rgb_tolerance" in value:
        out["minimumRGBTolerance"] = value["minimum_rgb_tolerance"]
    if "minimum_yuv" in value:
        out["minimumYUV"] = value["minimum_yuv"]
    return out


def deserialize_json(data: dict) -> ClipLimits:
    out: ClipLimits = {}  # type: ignore[typeddict-item]
    if "maximumRGBTolerance" in data:
        out["maximum_rgb_tolerance"] = data["maximumRGBTolerance"]
    if "maximumYUV" in data:
        out["maximum_yuv"] = data["maximumYUV"]
    if "minimumRGBTolerance" in data:
        out["minimum_rgb_tolerance"] = data["minimumRGBTolerance"]
    if "minimumYUV" in data:
        out["minimum_yuv"] = data["minimumYUV"]
    return out
