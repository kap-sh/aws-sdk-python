"""Generated from Smithy shape ``com.amazonaws.mediapackage#EncryptionContractConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.preset_speke20_audio
    import capo_mediapackage.types.preset_speke20_video


class EncryptionContractConfiguration(TypedDict, closed=True):
    preset_speke20_audio: NotRequired[
        "capo_mediapackage.types.preset_speke20_audio.PresetSpeke20Audio"
    ]
    """A collection of audio encryption presets."""
    preset_speke20_video: NotRequired[
        "capo_mediapackage.types.preset_speke20_video.PresetSpeke20Video"
    ]
    """A collection of video encryption presets."""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionContractConfiguration) -> dict:
    out: dict = {}
    if "preset_speke20_audio" in value:
        import capo_mediapackage.types.preset_speke20_audio

        out["presetSpeke20Audio"] = (
            capo_mediapackage.types.preset_speke20_audio.serialize_json(
                value["preset_speke20_audio"]
            )
        )
    if "preset_speke20_video" in value:
        import capo_mediapackage.types.preset_speke20_video

        out["presetSpeke20Video"] = (
            capo_mediapackage.types.preset_speke20_video.serialize_json(
                value["preset_speke20_video"]
            )
        )
    return out


def deserialize_json(data: dict) -> EncryptionContractConfiguration:
    out: EncryptionContractConfiguration = {}  # type: ignore[typeddict-item]
    if "presetSpeke20Audio" in data:
        import capo_mediapackage.types.preset_speke20_audio

        out["preset_speke20_audio"] = (
            capo_mediapackage.types.preset_speke20_audio.deserialize_json(
                data["presetSpeke20Audio"]
            )
        )
    if "presetSpeke20Video" in data:
        import capo_mediapackage.types.preset_speke20_video

        out["preset_speke20_video"] = (
            capo_mediapackage.types.preset_speke20_video.deserialize_json(
                data["presetSpeke20Video"]
            )
        )
    return out
