"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VorbisSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max2
    import aws_sdk_mediaconvert.types.__integer_min22050_max48000
    import aws_sdk_mediaconvert.types.__integer_min_negative1_max10


class VorbisSettings(TypedDict, closed=True):
    channels: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2.__integerMin0Max2"
    ]
    """Optional. Specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono on the console gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 0, 1, and 2. The default value is 2."""
    sample_rate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min22050_max48000.__integerMin22050Max48000"
    ]
    """Optional. Specify the audio sample rate in Hz. Valid values are 22050, 32000, 44100, and 48000. The default value is 48000."""
    vbr_quality: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative1_max10.__integerMinNegative1Max10"
    ]
    """Optional. Specify the variable audio quality of this Vorbis output from -1 (lowest quality, ~45 kbit/s) to 10 (highest quality, ~500 kbit/s). The default value is 4 (~128 kbit/s). Values 5 and 6 are approximately 160 and 192 kbit/s, respectively."""


# --- restJson1 ser/de ---
def serialize_json(value: VorbisSettings) -> dict:
    out: dict = {}
    if "channels" in value:
        out["channels"] = value["channels"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    if "vbr_quality" in value:
        out["vbrQuality"] = value["vbr_quality"]
    return out


def deserialize_json(data: dict) -> VorbisSettings:
    out: VorbisSettings = {}  # type: ignore[typeddict-item]
    if "channels" in data:
        out["channels"] = data["channels"]
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    if "vbrQuality" in data:
        out["vbr_quality"] = data["vbrQuality"]
    return out
