"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AutomatedAbrSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__double_min1_max10
    import aws_sdk_mediaconvert.types.__integer_min3_max15
    import aws_sdk_mediaconvert.types.__integer_min100000_max100000000
    import aws_sdk_mediaconvert.types.__list_of_automated_abr_rule


class AutomatedAbrSettings(TypedDict, closed=True):
    max_abr_bitrate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min100000_max100000000.__integerMin100000Max100000000"
    ]
    """Specify the maximum average bitrate for MediaConvert to use in your automated ABR stack. If you don't specify a value, MediaConvert uses 8,000,000 (8 mb/s) by default. The average bitrate of your highest-quality rendition will be equal to or below this value, depending on the quality, complexity, and resolution of your content. Note that the instantaneous maximum bitrate may vary above the value that you specify."""
    max_quality_level: NotRequired[
        "aws_sdk_mediaconvert.types.__double_min1_max10.__doubleMin1Max10"
    ]
    """Optional. Specify the QVBR quality level to use for all renditions in your automated ABR stack. To have MediaConvert automatically determine the quality level: Leave blank. To manually specify a quality level: Enter a value from 1 to 10. MediaConvert will use a quality level up to the value that you specify, depending on your source. For more information about QVBR quality levels, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/qvbr-guidelines.html"""
    max_renditions: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min3_max15.__integerMin3Max15"
    ]
    """Optional. The maximum number of renditions that MediaConvert will create in your automated ABR stack. The number of renditions is determined automatically, based on analysis of each job, but will never exceed this limit. When you set this to Auto in the console, which is equivalent to excluding it from your JSON job specification, MediaConvert defaults to a limit of 15."""
    min_abr_bitrate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min100000_max100000000.__integerMin100000Max100000000"
    ]
    """Specify the minimum average bitrate for MediaConvert to use in your automated ABR stack. If you don't specify a value, MediaConvert uses 600,000 (600 kb/s) by default. The average bitrate of your lowest-quality rendition will be near this value. Note that the instantaneous minimum bitrate may vary below the value that you specify."""
    rules: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_automated_abr_rule.__listOfAutomatedAbrRule"
    ]
    """Optional. Use Automated ABR rules to specify restrictions for the rendition sizes MediaConvert will create in your ABR stack. You can use these rules if your ABR workflow has specific rendition size requirements, but you still want MediaConvert to optimize for video quality and overall file size."""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedAbrSettings) -> dict:
    out: dict = {}
    if "max_abr_bitrate" in value:
        out["maxAbrBitrate"] = value["max_abr_bitrate"]
    if "max_quality_level" in value:
        out["maxQualityLevel"] = value["max_quality_level"]
    if "max_renditions" in value:
        out["maxRenditions"] = value["max_renditions"]
    if "min_abr_bitrate" in value:
        out["minAbrBitrate"] = value["min_abr_bitrate"]
    if "rules" in value:
        import aws_sdk_mediaconvert.types.__list_of_automated_abr_rule

        out["rules"] = (
            aws_sdk_mediaconvert.types.__list_of_automated_abr_rule.serialize_json(
                value["rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedAbrSettings:
    out: AutomatedAbrSettings = {}  # type: ignore[typeddict-item]
    if "maxAbrBitrate" in data:
        out["max_abr_bitrate"] = data["maxAbrBitrate"]
    if "maxQualityLevel" in data:
        out["max_quality_level"] = data["maxQualityLevel"]
    if "maxRenditions" in data:
        out["max_renditions"] = data["maxRenditions"]
    if "minAbrBitrate" in data:
        out["min_abr_bitrate"] = data["minAbrBitrate"]
    if "rules" in data:
        import aws_sdk_mediaconvert.types.__list_of_automated_abr_rule

        out["rules"] = (
            aws_sdk_mediaconvert.types.__list_of_automated_abr_rule.deserialize_json(
                data["rules"]
            )
        )
    return out
