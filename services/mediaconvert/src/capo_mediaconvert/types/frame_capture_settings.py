"""Generated from Smithy shape ``com.amazonaws.mediaconvert#FrameCaptureSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min1_max100
    import capo_mediaconvert.types.__integer_min1_max10000000
    import capo_mediaconvert.types.__integer_min1_max2147483647


class FrameCaptureSettings(TypedDict, closed=True):
    framerate_denominator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.n.jpg where n is the 0-based sequence number of each Capture."""
    framerate_numerator: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
    ]
    """Frame capture will encode the first frame of the output stream, then one frame every framerateDenominator/framerateNumerator seconds. For example, settings of framerateNumerator = 1 and framerateDenominator = 3 (a rate of 1/3 frame per second) will capture the first frame, then 1 frame every 3s. Files will be named as filename.NNNNNNN.jpg where N is the 0-based frame sequence number zero padded to 7 decimal places."""
    max_captures: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max10000000.__integerMin1Max10000000"
    ]
    """Maximum number of captures (encoded jpg output files)."""
    quality: NotRequired[
        "capo_mediaconvert.types.__integer_min1_max100.__integerMin1Max100"
    ]
    """JPEG Quality - a higher value equals higher quality."""


# --- restJson1 ser/de ---
def serialize_json(value: FrameCaptureSettings) -> dict:
    out: dict = {}
    if "framerate_denominator" in value:
        out["framerateDenominator"] = value["framerate_denominator"]
    if "framerate_numerator" in value:
        out["framerateNumerator"] = value["framerate_numerator"]
    if "max_captures" in value:
        out["maxCaptures"] = value["max_captures"]
    if "quality" in value:
        out["quality"] = value["quality"]
    return out


def deserialize_json(data: dict) -> FrameCaptureSettings:
    out: FrameCaptureSettings = {}  # type: ignore[typeddict-item]
    if "framerateDenominator" in data:
        out["framerate_denominator"] = data["framerateDenominator"]
    if "framerateNumerator" in data:
        out["framerate_numerator"] = data["framerateNumerator"]
    if "maxCaptures" in data:
        out["max_captures"] = data["maxCaptures"]
    if "quality" in data:
        out["quality"] = data["quality"]
    return out
