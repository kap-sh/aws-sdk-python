"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CreatePresetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__map_of__string
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.preset_settings


class CreatePresetRequest(TypedDict, closed=True):
    category: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Optional. A category for the preset you are creating."""
    description: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Optional. A description of the preset you are creating."""
    name: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The name of the preset you are creating."""
    settings: NotRequired["aws_sdk_mediaconvert.types.preset_settings.PresetSettings"]
    """Settings for preset"""
    tags: NotRequired["aws_sdk_mediaconvert.types.__map_of__string.__mapOf__string"]
    """The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key."""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePresetRequest) -> dict:
    out: dict = {}
    if "category" in value:
        out["category"] = value["category"]
    if "description" in value:
        out["description"] = value["description"]
    if "name" in value:
        out["name"] = value["name"]
    if "settings" in value:
        import aws_sdk_mediaconvert.types.preset_settings

        out["settings"] = aws_sdk_mediaconvert.types.preset_settings.serialize_json(
            value["settings"]
        )
    if "tags" in value:
        import aws_sdk_mediaconvert.types.__map_of__string

        out["tags"] = aws_sdk_mediaconvert.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreatePresetRequest:
    out: CreatePresetRequest = {}  # type: ignore[typeddict-item]
    if "category" in data:
        out["category"] = data["category"]
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    if "settings" in data:
        import aws_sdk_mediaconvert.types.preset_settings

        out["settings"] = aws_sdk_mediaconvert.types.preset_settings.deserialize_json(
            data["settings"]
        )
    if "tags" in data:
        import aws_sdk_mediaconvert.types.__map_of__string

        out["tags"] = aws_sdk_mediaconvert.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
