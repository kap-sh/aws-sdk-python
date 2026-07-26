"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Preset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.__timestamp_unix
    import capo_mediaconvert.types.preset_settings
    import capo_mediaconvert.types.type


class Preset(TypedDict, closed=True):
    arn: NotRequired["capo_mediaconvert.types.__string.__string"]
    """An identifier for this resource that is unique within all of AWS."""
    category: NotRequired["capo_mediaconvert.types.__string.__string"]
    """An optional category you create to organize your presets."""
    created_at: NotRequired["capo_mediaconvert.types.__timestamp_unix.__timestampUnix"]
    """The timestamp in epoch seconds for preset creation."""
    description: NotRequired["capo_mediaconvert.types.__string.__string"]
    """An optional description you create for each preset."""
    last_updated: NotRequired[
        "capo_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The timestamp in epoch seconds when the preset was last updated."""
    name: NotRequired["capo_mediaconvert.types.__string.__string"]
    """A name you create for each preset. Each name must be unique within your account."""
    settings: NotRequired["capo_mediaconvert.types.preset_settings.PresetSettings"]
    """Settings for preset"""
    type: NotRequired["capo_mediaconvert.types.type.Type"]
    """A preset can be of two types: system or custom. System or built-in preset can't be modified or deleted by the user."""


# --- restJson1 ser/de ---
def serialize_json(value: Preset) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "category" in value:
        out["category"] = value["category"]
    if "created_at" in value:
        import capo_mediaconvert.types.__timestamp_unix

        out["createdAt"] = capo_mediaconvert.types.__timestamp_unix.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "last_updated" in value:
        import capo_mediaconvert.types.__timestamp_unix

        out["lastUpdated"] = capo_mediaconvert.types.__timestamp_unix.serialize_json(
            value["last_updated"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "settings" in value:
        import capo_mediaconvert.types.preset_settings

        out["settings"] = capo_mediaconvert.types.preset_settings.serialize_json(
            value["settings"]
        )
    if "type" in value:
        import capo_mediaconvert.types.type

        out["type"] = capo_mediaconvert.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> Preset:
    out: Preset = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "category" in data:
        out["category"] = data["category"]
    if "createdAt" in data:
        import capo_mediaconvert.types.__timestamp_unix

        out["created_at"] = capo_mediaconvert.types.__timestamp_unix.deserialize_json(
            data["createdAt"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "lastUpdated" in data:
        import capo_mediaconvert.types.__timestamp_unix

        out["last_updated"] = capo_mediaconvert.types.__timestamp_unix.deserialize_json(
            data["lastUpdated"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "settings" in data:
        import capo_mediaconvert.types.preset_settings

        out["settings"] = capo_mediaconvert.types.preset_settings.deserialize_json(
            data["settings"]
        )
    if "type" in data:
        import capo_mediaconvert.types.type

        out["type"] = capo_mediaconvert.types.type.deserialize_json(data["type"])
    return out
