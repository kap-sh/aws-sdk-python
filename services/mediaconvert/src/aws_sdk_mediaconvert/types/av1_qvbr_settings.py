"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Av1QvbrSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__double_min0_max1
    import aws_sdk_mediaconvert.types.__integer_min1_max10


class Av1QvbrSettings(TypedDict):
    qvbr_quality_level: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min1_max10.__integerMin1Max10"
    ]
    """Use this setting only when you set Rate control mode to QVBR. Specify the target quality level for this output. MediaConvert determines the right number of bits to use for each part of the video to maintain the video quality that you specify. When you keep the default value, AUTO, MediaConvert picks a quality level for you, based on characteristics of your input video. If you prefer to specify a quality level, specify a number from 1 through 10. Use higher numbers for greater quality. Level 10 results in nearly lossless compression. The quality level for most broadcast-quality transcodes is between 6 and 9. Optionally, to specify a value between whole numbers, also provide a value for the setting qvbrQualityLevelFineTune. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33."""
    qvbr_quality_level_fine_tune: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min0_max1.__doubleMin0Max1"
    ]
    """Optional. Specify a value here to set the QVBR quality to a level that is between whole numbers. For example, if you want your QVBR quality level to be 7.33, set qvbrQualityLevel to 7 and set qvbrQualityLevelFineTune to .33. MediaConvert rounds your QVBR quality level to the nearest third of a whole number. For example, if you set qvbrQualityLevel to 7 and you set qvbrQualityLevelFineTune to .25, your actual QVBR quality level is 7.33."""


# --- restJson1 ser/de ---
def serialize_json(value: Av1QvbrSettings) -> dict:
    out: dict = {}
    if "qvbr_quality_level" in value:
        out["qvbrQualityLevel"] = value["qvbr_quality_level"]
    if "qvbr_quality_level_fine_tune" in value:
        out["qvbrQualityLevelFineTune"] = value["qvbr_quality_level_fine_tune"]
    return out


def deserialize_json(data: dict) -> Av1QvbrSettings:
    out: Av1QvbrSettings = {}  # type: ignore[typeddict-item]
    if "qvbrQualityLevel" in data:
        out["qvbr_quality_level"] = data["qvbrQualityLevel"]
    if "qvbrQualityLevelFineTune" in data:
        out["qvbr_quality_level_fine_tune"] = data["qvbrQualityLevelFineTune"]
    return out
