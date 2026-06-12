"""Generated from Smithy shape ``com.amazonaws.medialive#AudioWatermarkSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.nielsen_watermarks_settings


class AudioWatermarkSettings(TypedDict):
    nielsen_watermarks_settings: NotRequired[
        "aws_sdk_medialive.types.nielsen_watermarks_settings.NielsenWatermarksSettings"
    ]
    """Settings to configure Nielsen Watermarks in the audio encode"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioWatermarkSettings) -> dict:
    out: dict = {}
    if "nielsen_watermarks_settings" in value:
        import aws_sdk_medialive.types.nielsen_watermarks_settings

        out["nielsenWatermarksSettings"] = (
            aws_sdk_medialive.types.nielsen_watermarks_settings.serialize_json(
                value["nielsen_watermarks_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioWatermarkSettings:
    out: AudioWatermarkSettings = {}  # type: ignore[typeddict-item]
    if "nielsenWatermarksSettings" in data:
        import aws_sdk_medialive.types.nielsen_watermarks_settings

        out["nielsen_watermarks_settings"] = (
            aws_sdk_medialive.types.nielsen_watermarks_settings.deserialize_json(
                data["nielsenWatermarksSettings"]
            )
        )
    return out
