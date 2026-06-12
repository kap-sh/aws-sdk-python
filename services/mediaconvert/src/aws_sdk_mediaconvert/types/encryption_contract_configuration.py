"""Generated from Smithy shape ``com.amazonaws.mediaconvert#EncryptionContractConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.preset_speke20_audio
    import aws_sdk_mediaconvert.types.preset_speke20_video


class EncryptionContractConfiguration(TypedDict):
    speke_audio_preset: NotRequired[
        "aws_sdk_mediaconvert.types.preset_speke20_audio.PresetSpeke20Audio"
    ]
    """Specify which SPEKE version 2.0 audio preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html To encrypt to your audio outputs, choose from the following: Audio preset 1, Audio preset 2, or Audio preset 3. To encrypt your audio outputs, using the same content key for both your audio and video outputs: Choose Shared. When you do, you must also set SPEKE v2.0 video preset to Shared. To not encrypt your audio outputs: Choose Unencrypted. When you do, to encrypt your video outputs, you must also specify a SPEKE v2.0 video preset (other than Shared or Unencrypted)."""
    speke_video_preset: NotRequired[
        "aws_sdk_mediaconvert.types.preset_speke20_video.PresetSpeke20Video"
    ]
    """Specify which SPEKE version 2.0 video preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html To encrypt to your video outputs, choose from the following: Video preset 1, Video preset 2, Video preset 3, Video preset 4, Video preset 5, Video preset 6, Video preset 7, or Video preset 8. To encrypt your video outputs, using the same content key for both your video and audio outputs: Choose Shared. When you do, you must also set SPEKE v2.0 audio preset to Shared. To not encrypt your video outputs: Choose Unencrypted. When you do, to encrypt your audio outputs, you must also specify a SPEKE v2.0 audio preset (other than Shared or Unencrypted)."""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionContractConfiguration) -> dict:
    out: dict = {}
    if "speke_audio_preset" in value:
        import aws_sdk_mediaconvert.types.preset_speke20_audio

        out["spekeAudioPreset"] = (
            aws_sdk_mediaconvert.types.preset_speke20_audio.serialize_json(
                value["speke_audio_preset"]
            )
        )
    if "speke_video_preset" in value:
        import aws_sdk_mediaconvert.types.preset_speke20_video

        out["spekeVideoPreset"] = (
            aws_sdk_mediaconvert.types.preset_speke20_video.serialize_json(
                value["speke_video_preset"]
            )
        )
    return out


def deserialize_json(data: dict) -> EncryptionContractConfiguration:
    out: EncryptionContractConfiguration = {}  # type: ignore[typeddict-item]
    if "spekeAudioPreset" in data:
        import aws_sdk_mediaconvert.types.preset_speke20_audio

        out["speke_audio_preset"] = (
            aws_sdk_mediaconvert.types.preset_speke20_audio.deserialize_json(
                data["spekeAudioPreset"]
            )
        )
    if "spekeVideoPreset" in data:
        import aws_sdk_mediaconvert.types.preset_speke20_video

        out["speke_video_preset"] = (
            aws_sdk_mediaconvert.types.preset_speke20_video.deserialize_json(
                data["spekeVideoPreset"]
            )
        )
    return out
