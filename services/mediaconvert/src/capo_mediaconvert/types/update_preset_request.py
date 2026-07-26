"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UpdatePresetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.preset_settings


class UpdatePresetRequest(TypedDict, closed=True):
    category: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The new category for the preset, if you are changing it."""
    description: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The new description for the preset, if you are changing it."""
    name: "capo_mediaconvert.types.__string.__string"
    """The name of the preset you are modifying."""
    settings: NotRequired["capo_mediaconvert.types.preset_settings.PresetSettings"]
    """Settings for preset"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePresetRequest) -> dict:
    out: dict = {}
    if "category" in value:
        out["category"] = value["category"]
    if "description" in value:
        out["description"] = value["description"]
    if "settings" in value:
        import capo_mediaconvert.types.preset_settings

        out["settings"] = capo_mediaconvert.types.preset_settings.serialize_json(
            value["settings"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePresetRequest:
    out: UpdatePresetRequest = {}  # type: ignore[typeddict-item]
    if "category" in data:
        out["category"] = data["category"]
    if "description" in data:
        out["description"] = data["description"]
    if "settings" in data:
        import capo_mediaconvert.types.preset_settings

        out["settings"] = capo_mediaconvert.types.preset_settings.deserialize_json(
            data["settings"]
        )
    return out
