"""Generated from Smithy shape ``com.amazonaws.medialive#AudioWatermarkSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.nielsen_watermarks_settings


class AudioWatermarkSettings(TypedDict, closed=True):
    nielsen_watermarks_settings: NotRequired[
        "capo_medialive.types.nielsen_watermarks_settings.NielsenWatermarksSettings"
    ]
    """Settings to configure Nielsen Watermarks in the audio encode"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioWatermarkSettings) -> dict:
    out: dict = {}
    if "nielsen_watermarks_settings" in value:
        import capo_medialive.types.nielsen_watermarks_settings

        out["nielsenWatermarksSettings"] = (
            capo_medialive.types.nielsen_watermarks_settings.serialize_json(
                value["nielsen_watermarks_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioWatermarkSettings:
    out: AudioWatermarkSettings = {}  # type: ignore[typeddict-item]
    if "nielsenWatermarksSettings" in data:
        import capo_medialive.types.nielsen_watermarks_settings

        out["nielsen_watermarks_settings"] = (
            capo_medialive.types.nielsen_watermarks_settings.deserialize_json(
                data["nielsenWatermarksSettings"]
            )
        )
    return out
