"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Hdr10Metadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max50000
    import aws_sdk_mediaconvert.types.__integer_min0_max65535
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647


class Hdr10Metadata(TypedDict):
    blue_primary_x: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max50000.__integerMin0Max50000"
    ]
    """HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction."""
    blue_primary_y: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max50000.__integerMin0Max50000"
    ]
    """HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction."""
    green_primary_x: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max50000.__integerMin0Max50000"
    ]
    """HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction."""
    green_primary_y: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max50000.__integerMin0Max50000"
    ]
    """HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction."""
    max_content_light_level: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """Maximum light level among all samples in the coded video sequence, in units of candelas per square meter. This setting doesn't have a default value; you must specify a value that is suitable for the content."""
    max_frame_average_light_level: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """Maximum average light level of any frame in the coded video sequence, in units of candelas per square meter. This setting doesn't have a default value; you must specify a value that is suitable for the content."""
    max_luminance: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Nominal maximum mastering display luminance in units of of 0.0001 candelas per square meter."""
    min_luminance: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Nominal minimum mastering display luminance in units of of 0.0001 candelas per square meter"""
    red_primary_x: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max50000.__integerMin0Max50000"
    ]
    """HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction."""
    red_primary_y: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max50000.__integerMin0Max50000"
    ]
    """HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction."""
    white_point_x: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max50000.__integerMin0Max50000"
    ]
    """HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction."""
    white_point_y: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max50000.__integerMin0Max50000"
    ]
    """HDR Master Display Information must be provided by a color grader, using color grading tools. Range is 0 to 50,000, each increment represents 0.00002 in CIE1931 color coordinate. Note that this setting is not for color correction."""


# --- restJson1 ser/de ---
def serialize_json(value: Hdr10Metadata) -> dict:
    out: dict = {}
    if "blue_primary_x" in value:
        out["bluePrimaryX"] = value["blue_primary_x"]
    if "blue_primary_y" in value:
        out["bluePrimaryY"] = value["blue_primary_y"]
    if "green_primary_x" in value:
        out["greenPrimaryX"] = value["green_primary_x"]
    if "green_primary_y" in value:
        out["greenPrimaryY"] = value["green_primary_y"]
    if "max_content_light_level" in value:
        out["maxContentLightLevel"] = value["max_content_light_level"]
    if "max_frame_average_light_level" in value:
        out["maxFrameAverageLightLevel"] = value["max_frame_average_light_level"]
    if "max_luminance" in value:
        out["maxLuminance"] = value["max_luminance"]
    if "min_luminance" in value:
        out["minLuminance"] = value["min_luminance"]
    if "red_primary_x" in value:
        out["redPrimaryX"] = value["red_primary_x"]
    if "red_primary_y" in value:
        out["redPrimaryY"] = value["red_primary_y"]
    if "white_point_x" in value:
        out["whitePointX"] = value["white_point_x"]
    if "white_point_y" in value:
        out["whitePointY"] = value["white_point_y"]
    return out


def deserialize_json(data: dict) -> Hdr10Metadata:
    out: Hdr10Metadata = {}  # type: ignore[typeddict-item]
    if "bluePrimaryX" in data:
        out["blue_primary_x"] = data["bluePrimaryX"]
    if "bluePrimaryY" in data:
        out["blue_primary_y"] = data["bluePrimaryY"]
    if "greenPrimaryX" in data:
        out["green_primary_x"] = data["greenPrimaryX"]
    if "greenPrimaryY" in data:
        out["green_primary_y"] = data["greenPrimaryY"]
    if "maxContentLightLevel" in data:
        out["max_content_light_level"] = data["maxContentLightLevel"]
    if "maxFrameAverageLightLevel" in data:
        out["max_frame_average_light_level"] = data["maxFrameAverageLightLevel"]
    if "maxLuminance" in data:
        out["max_luminance"] = data["maxLuminance"]
    if "minLuminance" in data:
        out["min_luminance"] = data["minLuminance"]
    if "redPrimaryX" in data:
        out["red_primary_x"] = data["redPrimaryX"]
    if "redPrimaryY" in data:
        out["red_primary_y"] = data["redPrimaryY"]
    if "whitePointX" in data:
        out["white_point_x"] = data["whitePointX"]
    if "whitePointY" in data:
        out["white_point_y"] = data["whitePointY"]
    return out
