"""Generated from Smithy shape ``com.amazonaws.mediaconvert#WavSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max64
    import aws_sdk_mediaconvert.types.__integer_min16_max24
    import aws_sdk_mediaconvert.types.__integer_min8000_max192000
    import aws_sdk_mediaconvert.types.wav_format


class WavSettings(TypedDict):
    bit_depth: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min16_max24.__integerMin16Max24"
    ]
    """Specify Bit depth, in bits per sample, to choose the encoding quality for this audio track."""
    channels: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max64.__integerMin0Max64"
    ]
    """Specify the number of channels in this output audio track. Valid values are 0, 1, and even numbers up to 64. Choose 0 to follow the number of channels from your input audio. Otherwise, manually choose from 1, 2, 4, 6, and so on, up to 64."""
    format: NotRequired["aws_sdk_mediaconvert.types.wav_format.WavFormat"]
    """Specify the file format for your wave audio output. To use a RIFF wave format: Keep the default value, RIFF. If your output audio is likely to exceed 4GB in file size, or if you otherwise need the extended support of the RF64 format: Choose RF64. If your player only supports the extensible wave format: Choose Extensible."""
    sample_rate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min8000_max192000.__integerMin8000Max192000"
    ]
    """Sample rate in Hz."""


# --- restJson1 ser/de ---
def serialize_json(value: WavSettings) -> dict:
    out: dict = {}
    if "bit_depth" in value:
        out["bitDepth"] = value["bit_depth"]
    if "channels" in value:
        out["channels"] = value["channels"]
    if "format" in value:
        import aws_sdk_mediaconvert.types.wav_format

        out["format"] = aws_sdk_mediaconvert.types.wav_format.serialize_json(
            value["format"]
        )
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    return out


def deserialize_json(data: dict) -> WavSettings:
    out: WavSettings = {}  # type: ignore[typeddict-item]
    if "bitDepth" in data:
        out["bit_depth"] = data["bitDepth"]
    if "channels" in data:
        out["channels"] = data["channels"]
    if "format" in data:
        import aws_sdk_mediaconvert.types.wav_format

        out["format"] = aws_sdk_mediaconvert.types.wav_format.deserialize_json(
            data["format"]
        )
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    return out
