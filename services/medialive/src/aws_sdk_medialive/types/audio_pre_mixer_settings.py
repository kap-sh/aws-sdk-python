"""Generated from Smithy shape ``com.amazonaws.medialive#AudioPreMixerSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double_min_negative60_max60
    import aws_sdk_medialive.types.__integer_min1_max16
    import aws_sdk_medialive.types.audio_normalization_settings
    import aws_sdk_medialive.types.remix_settings


class AudioPreMixerSettings(TypedDict, closed=True):
    audio_normalization_settings: NotRequired[
        "aws_sdk_medialive.types.audio_normalization_settings.AudioNormalizationSettings"
    ]
    """Audio normalization settings for loudness control. When specified, audio loudness will be normalized according to the chosen algorithm."""
    channels: NotRequired[
        "aws_sdk_medialive.types.__integer_min1_max16.__integerMin1Max16"
    ]
    """Number of audio channels. If specified, the audio will be remixed to match this channel count. Ignored if remixSettings is specified."""
    gain_db: NotRequired[
        "aws_sdk_medialive.types.__double_min_negative60_max60.__doubleMinNegative60Max60"
    ]
    """Gain adjustment in dB to apply. Range: -60 to +60 dB"""
    remix_settings: NotRequired["aws_sdk_medialive.types.remix_settings.RemixSettings"]
    """Settings that control how input audio channels are remixed. When specified, allows fine-grained control over channel mapping and gain levels. Takes precedence over the 'channels' setting."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioPreMixerSettings) -> dict:
    out: dict = {}
    if "audio_normalization_settings" in value:
        import aws_sdk_medialive.types.audio_normalization_settings

        out["audioNormalizationSettings"] = (
            aws_sdk_medialive.types.audio_normalization_settings.serialize_json(
                value["audio_normalization_settings"]
            )
        )
    if "channels" in value:
        out["channels"] = value["channels"]
    if "gain_db" in value:
        out["gainDb"] = value["gain_db"]
    if "remix_settings" in value:
        import aws_sdk_medialive.types.remix_settings

        out["remixSettings"] = aws_sdk_medialive.types.remix_settings.serialize_json(
            value["remix_settings"]
        )
    return out


def deserialize_json(data: dict) -> AudioPreMixerSettings:
    out: AudioPreMixerSettings = {}  # type: ignore[typeddict-item]
    if "audioNormalizationSettings" in data:
        import aws_sdk_medialive.types.audio_normalization_settings

        out["audio_normalization_settings"] = (
            aws_sdk_medialive.types.audio_normalization_settings.deserialize_json(
                data["audioNormalizationSettings"]
            )
        )
    if "channels" in data:
        out["channels"] = data["channels"]
    if "gainDb" in data:
        out["gain_db"] = data["gainDb"]
    if "remixSettings" in data:
        import aws_sdk_medialive.types.remix_settings

        out["remix_settings"] = aws_sdk_medialive.types.remix_settings.deserialize_json(
            data["remixSettings"]
        )
    return out
