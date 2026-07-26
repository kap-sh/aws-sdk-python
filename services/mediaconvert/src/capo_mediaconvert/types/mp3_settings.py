"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp3Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max2
    import capo_mediaconvert.types.__integer_min0_max9
    import capo_mediaconvert.types.__integer_min16000_max320000
    import capo_mediaconvert.types.__integer_min22050_max48000
    import capo_mediaconvert.types.mp3_rate_control_mode


class Mp3Settings(TypedDict, closed=True):
    bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min16000_max320000.__integerMin16000Max320000"
    ]
    """Specify the average bitrate in bits per second."""
    channels: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2.__integerMin0Max2"
    ]
    """Specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono gives you 1 output channel; choosing Stereo gives you 2. In the API, valid values are 0, 1, and 2."""
    rate_control_mode: NotRequired[
        "capo_mediaconvert.types.mp3_rate_control_mode.Mp3RateControlMode"
    ]
    """Specify whether the service encodes this MP3 audio output with a constant bitrate (CBR) or a variable bitrate (VBR)."""
    sample_rate: NotRequired[
        "capo_mediaconvert.types.__integer_min22050_max48000.__integerMin22050Max48000"
    ]
    """Sample rate in Hz."""
    vbr_quality: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max9.__integerMin0Max9"
    ]
    """Required when you set Bitrate control mode to VBR. Specify the audio quality of this MP3 output from 0 (highest quality) to 9 (lowest quality)."""


# --- restJson1 ser/de ---
def serialize_json(value: Mp3Settings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "channels" in value:
        out["channels"] = value["channels"]
    if "rate_control_mode" in value:
        import capo_mediaconvert.types.mp3_rate_control_mode

        out["rateControlMode"] = (
            capo_mediaconvert.types.mp3_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    if "vbr_quality" in value:
        out["vbrQuality"] = value["vbr_quality"]
    return out


def deserialize_json(data: dict) -> Mp3Settings:
    out: Mp3Settings = {}  # type: ignore[typeddict-item]
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "channels" in data:
        out["channels"] = data["channels"]
    if "rateControlMode" in data:
        import capo_mediaconvert.types.mp3_rate_control_mode

        out["rate_control_mode"] = (
            capo_mediaconvert.types.mp3_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    if "vbrQuality" in data:
        out["vbr_quality"] = data["vbrQuality"]
    return out
