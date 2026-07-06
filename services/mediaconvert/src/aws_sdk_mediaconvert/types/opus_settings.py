"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OpusSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max2
    import aws_sdk_mediaconvert.types.__integer_min16000_max48000
    import aws_sdk_mediaconvert.types.__integer_min32000_max192000


class OpusSettings(TypedDict, closed=True):
    bitrate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32000_max192000.__integerMin32000Max192000"
    ]
    """Optional. Specify the average bitrate in bits per second. Valid values are multiples of 8000, from 32000 through 192000. The default value is 96000, which we recommend for quality and bandwidth."""
    channels: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2.__integerMin0Max2"
    ]
    """Specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 0, 1, and 2."""
    sample_rate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min16000_max48000.__integerMin16000Max48000"
    ]
    """Optional. Sample rate in Hz. Valid values are 16000, 24000, and 48000. The default value is 48000."""


# --- restJson1 ser/de ---
def serialize_json(value: OpusSettings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "channels" in value:
        out["channels"] = value["channels"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    return out


def deserialize_json(data: dict) -> OpusSettings:
    out: OpusSettings = {}  # type: ignore[typeddict-item]
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "channels" in data:
        out["channels"] = data["channels"]
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    return out
