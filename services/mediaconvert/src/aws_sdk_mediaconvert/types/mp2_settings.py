"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp2Settings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max2
    import aws_sdk_mediaconvert.types.__integer_min32000_max48000
    import aws_sdk_mediaconvert.types.__integer_min32000_max384000
    import aws_sdk_mediaconvert.types.mp2_audio_description_mix


class Mp2Settings(TypedDict):
    audio_description_mix: NotRequired[
        "aws_sdk_mediaconvert.types.mp2_audio_description_mix.Mp2AudioDescriptionMix"
    ]
    """Choose BROADCASTER_MIXED_AD when the input contains pre-mixed main audio + audio description (AD) as a stereo pair. The value for AudioType will be set to 3, which signals to downstream systems that this stream contains \"broadcaster mixed AD\". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. When you choose BROADCASTER_MIXED_AD, the encoder ignores any values you provide in AudioType and FollowInputAudioType. Choose NONE when the input does not contain pre-mixed audio + audio description (AD). In this case, the encoder will use any values you provide for AudioType and FollowInputAudioType."""
    bitrate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32000_max384000.__integerMin32000Max384000"
    ]
    """Specify the average bitrate in bits per second."""
    channels: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2.__integerMin0Max2"
    ]
    """Set Channels to specify the number of channels in this output audio track. Choosing Follow input will use the number of channels found in the audio source; choosing Mono will give you 1 output channel; choosing Stereo will give you 2. In the API, valid values are 0, 1, and 2."""
    sample_rate: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min32000_max48000.__integerMin32000Max48000"
    ]
    """Sample rate in Hz."""


# --- restJson1 ser/de ---
def serialize_json(value: Mp2Settings) -> dict:
    out: dict = {}
    if "audio_description_mix" in value:
        import aws_sdk_mediaconvert.types.mp2_audio_description_mix

        out["audioDescriptionMix"] = (
            aws_sdk_mediaconvert.types.mp2_audio_description_mix.serialize_json(
                value["audio_description_mix"]
            )
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "channels" in value:
        out["channels"] = value["channels"]
    if "sample_rate" in value:
        out["sampleRate"] = value["sample_rate"]
    return out


def deserialize_json(data: dict) -> Mp2Settings:
    out: Mp2Settings = {}  # type: ignore[typeddict-item]
    if "audioDescriptionMix" in data:
        import aws_sdk_mediaconvert.types.mp2_audio_description_mix

        out["audio_description_mix"] = (
            aws_sdk_mediaconvert.types.mp2_audio_description_mix.deserialize_json(
                data["audioDescriptionMix"]
            )
        )
    if "bitrate" in data:
        out["bitrate"] = data["bitrate"]
    if "channels" in data:
        out["channels"] = data["channels"]
    if "sampleRate" in data:
        out["sample_rate"] = data["sampleRate"]
    return out
