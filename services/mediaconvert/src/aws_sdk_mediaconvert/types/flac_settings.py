"""Generated from Smithy shape ``com.amazonaws.mediaconvert#FlacSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max8
    import aws_sdk_mediaconvert.types.__integer_min16_max24
    import aws_sdk_mediaconvert.types.__integer_min22050_max192000


class FlacSettings(TypedDict):
    bit_depth: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min16_max24.__integerMin16Max24"
    ]
    """Specify Bit depth (BitDepth), in bits per sample, to choose the encoding quality for this audio track."""
    channels: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max8.__integerMin0Max8"
    ]
    """Specify the number of channels in this output audio track. Valid values are 0, 1, and even numbers up to 8. Choose 0 to follow the number of channels from your input audio. Otherwise, manually choose from 1, 2, 4, 6, and 8."""
    sample_rate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min22050_max192000.__integerMin22050Max192000"
    ]
    """Sample rate in Hz."""


# --- restJson1 ser/de ---
def serialize_json(value: FlacSettings) -> dict:
    out: dict = {}
    if "bit_depth" in value:
        out["bitDepth"] = value["bit_depth"]
    if "channels" in value:
        out["channels"] = value["channels"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    return out


def deserialize_json(data: dict) -> FlacSettings:
    out: FlacSettings = {}  # type: ignore[typeddict-item]
    if "bitDepth" in data:
        out["bit_depth"] = data["bitDepth"]
    if "channels" in data:
        out["channels"] = data["channels"]
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    return out
