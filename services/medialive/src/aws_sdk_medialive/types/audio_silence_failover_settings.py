"""Generated from Smithy shape ``com.amazonaws.medialive#AudioSilenceFailoverSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min1000
    import aws_sdk_medialive.types.__string


class AudioSilenceFailoverSettings(TypedDict, closed=True):
    audio_selector_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the audio selector in the input that MediaLive should monitor to detect silence. Select your most important rendition. If you didn't create an audio selector in this input, leave blank."""
    audio_silence_threshold_msec: NotRequired[
        "aws_sdk_medialive.types.__integer_min1000.__integerMin1000"
    ]
    """The amount of time (in milliseconds) that the active input must be silent before automatic input failover occurs. Silence is defined as audio loss or audio quieter than -50 dBFS."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioSilenceFailoverSettings) -> dict:
    out: dict = {}
    if "audio_selector_name" in value:
        out["audioSelectorName"] = value["audio_selector_name"]
    if "audio_silence_threshold_msec" in value:
        out["audioSilenceThresholdMsec"] = value["audio_silence_threshold_msec"]
    return out


def deserialize_json(data: dict) -> AudioSilenceFailoverSettings:
    out: AudioSilenceFailoverSettings = {}  # type: ignore[typeddict-item]
    if "audioSelectorName" in data:
        out["audio_selector_name"] = data["audioSelectorName"]
    if "audioSilenceThresholdMsec" in data:
        out["audio_silence_threshold_msec"] = data["audioSilenceThresholdMsec"]
    return out
