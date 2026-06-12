"""Generated from Smithy shape ``com.amazonaws.mediapackage#EncryptionContractConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.preset_speke20_audio
    import aws_sdk_mediapackage.types.preset_speke20_video


class EncryptionContractConfiguration(TypedDict):
    preset_speke20_audio: NotRequired[
        "aws_sdk_mediapackage.types.preset_speke20_audio.PresetSpeke20Audio"
    ]
    """A collection of audio encryption presets."""
    preset_speke20_video: NotRequired[
        "aws_sdk_mediapackage.types.preset_speke20_video.PresetSpeke20Video"
    ]
    """A collection of video encryption presets."""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionContractConfiguration) -> dict:
    out: dict = {}
    if "preset_speke20_audio" in value:
        import aws_sdk_mediapackage.types.preset_speke20_audio

        out["presetSpeke20Audio"] = (
            aws_sdk_mediapackage.types.preset_speke20_audio.serialize_json(
                value["preset_speke20_audio"]
            )
        )
    if "preset_speke20_video" in value:
        import aws_sdk_mediapackage.types.preset_speke20_video

        out["presetSpeke20Video"] = (
            aws_sdk_mediapackage.types.preset_speke20_video.serialize_json(
                value["preset_speke20_video"]
            )
        )
    return out


def deserialize_json(data: dict) -> EncryptionContractConfiguration:
    out: EncryptionContractConfiguration = {}  # type: ignore[typeddict-item]
    if "presetSpeke20Audio" in data:
        import aws_sdk_mediapackage.types.preset_speke20_audio

        out["preset_speke20_audio"] = (
            aws_sdk_mediapackage.types.preset_speke20_audio.deserialize_json(
                data["presetSpeke20Audio"]
            )
        )
    if "presetSpeke20Video" in data:
        import aws_sdk_mediapackage.types.preset_speke20_video

        out["preset_speke20_video"] = (
            aws_sdk_mediapackage.types.preset_speke20_video.deserialize_json(
                data["presetSpeke20Video"]
            )
        )
    return out
