"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MasteringDisplayColorVolume``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer
    import aws_sdk_mediaconvert.types.__long


class MasteringDisplayColorVolume(TypedDict):
    blue_primary_x: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Blue primary chromaticity x coordinate, in units of 0.00002."""
    blue_primary_y: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Blue primary chromaticity y coordinate, in units of 0.00002."""
    green_primary_x: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Green primary chromaticity x coordinate, in units of 0.00002."""
    green_primary_y: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Green primary chromaticity y coordinate, in units of 0.00002."""
    max_luminance: NotRequired["aws_sdk_mediaconvert.types.__long.__long"]
    """Maximum display mastering luminance, in units of 0.0001 cd/m²."""
    min_luminance: NotRequired["aws_sdk_mediaconvert.types.__long.__long"]
    """Minimum display mastering luminance, in units of 0.0001 cd/m²."""
    red_primary_x: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Red primary chromaticity x coordinate, in units of 0.00002."""
    red_primary_y: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """Red primary chromaticity y coordinate, in units of 0.00002."""
    white_point_x: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """White point chromaticity x coordinate, in units of 0.00002."""
    white_point_y: NotRequired["aws_sdk_mediaconvert.types.__integer.__integer"]
    """White point chromaticity y coordinate, in units of 0.00002."""


# --- restJson1 ser/de ---
def serialize_json(value: MasteringDisplayColorVolume) -> dict:
    out: dict = {}
    if "blue_primary_x" in value:
        out["bluePrimaryX"] = value["blue_primary_x"]
    if "blue_primary_y" in value:
        out["bluePrimaryY"] = value["blue_primary_y"]
    if "green_primary_x" in value:
        out["greenPrimaryX"] = value["green_primary_x"]
    if "green_primary_y" in value:
        out["greenPrimaryY"] = value["green_primary_y"]
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


def deserialize_json(data: dict) -> MasteringDisplayColorVolume:
    out: MasteringDisplayColorVolume = {}  # type: ignore[typeddict-item]
    if "bluePrimaryX" in data:
        out["blue_primary_x"] = data["bluePrimaryX"]
    if "bluePrimaryY" in data:
        out["blue_primary_y"] = data["bluePrimaryY"]
    if "greenPrimaryX" in data:
        out["green_primary_x"] = data["greenPrimaryX"]
    if "greenPrimaryY" in data:
        out["green_primary_y"] = data["greenPrimaryY"]
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
