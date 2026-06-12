"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AvailBlanking``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string_min14_pattern_s3_bmp_bmp_png_png_https_bmp_bmp_png_png


class AvailBlanking(TypedDict):
    avail_blanking_image: NotRequired[
        "aws_sdk_mediaconvert.types.__string_min14_pattern_s3_bmp_bmp_png_png_https_bmp_bmp_png_png.__stringMin14PatternS3BmpBMPPngPNGHttpsBmpBMPPngPNG"
    ]
    """Blanking image to be used. Leave empty for solid black. Only bmp and png images are supported."""


# --- restJson1 ser/de ---
def serialize_json(value: AvailBlanking) -> dict:
    out: dict = {}
    if "avail_blanking_image" in value:
        out["availBlankingImage"] = value["avail_blanking_image"]
    return out


def deserialize_json(data: dict) -> AvailBlanking:
    out: AvailBlanking = {}  # type: ignore[typeddict-item]
    if "availBlankingImage" in data:
        out["avail_blanking_image"] = data["availBlankingImage"]
    return out
