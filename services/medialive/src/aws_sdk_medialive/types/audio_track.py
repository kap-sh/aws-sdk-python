"""Generated from Smithy shape ``com.amazonaws.medialive#AudioTrack``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min1
    import aws_sdk_medialive.types.audio_pre_mixer_settings


class AudioTrack(TypedDict):
    track: NotRequired["aws_sdk_medialive.types.__integer_min1.__integerMin1"]
    """1-based integer value that maps to a specific audio track"""
    premix_settings: NotRequired[
        "aws_sdk_medialive.types.audio_pre_mixer_settings.AudioPreMixerSettings"
    ]
    """Optional audio pre-mixer settings for this track. When specified, allows per-track audio processing including channel remixing, gain adjustment, and loudness normalization before interleaving."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioTrack) -> dict:
    out: dict = {}
    if "track" in value:
        out["track"] = value["track"]
    if "premix_settings" in value:
        import aws_sdk_medialive.types.audio_pre_mixer_settings

        out["premixSettings"] = (
            aws_sdk_medialive.types.audio_pre_mixer_settings.serialize_json(
                value["premix_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioTrack:
    out: AudioTrack = {}  # type: ignore[typeddict-item]
    if "track" in data:
        out["track"] = data["track"]
    if "premixSettings" in data:
        import aws_sdk_medialive.types.audio_pre_mixer_settings

        out["premix_settings"] = (
            aws_sdk_medialive.types.audio_pre_mixer_settings.deserialize_json(
                data["premixSettings"]
            )
        )
    return out
