"""Generated from Smithy shape ``com.amazonaws.medialive#ArchiveOutputSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.archive_container_settings


class ArchiveOutputSettings(TypedDict):
    container_settings: NotRequired[
        "aws_sdk_medialive.types.archive_container_settings.ArchiveContainerSettings"
    ]
    """Container for this output. Can be auto-detected from extension field."""
    extension: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Output file extension. If excluded, this will be auto-selected from the container type."""
    name_modifier: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """String concatenated to the end of the destination filename. Required for multiple outputs of the same type."""


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveOutputSettings) -> dict:
    out: dict = {}
    if "container_settings" in value:
        import aws_sdk_medialive.types.archive_container_settings

        out["containerSettings"] = (
            aws_sdk_medialive.types.archive_container_settings.serialize_json(
                value["container_settings"]
            )
        )
    if "extension" in value:
        out["extension"] = value["extension"]
    if "name_modifier" in value:
        out["nameModifier"] = value["name_modifier"]
    return out


def deserialize_json(data: dict) -> ArchiveOutputSettings:
    out: ArchiveOutputSettings = {}  # type: ignore[typeddict-item]
    if "containerSettings" in data:
        import aws_sdk_medialive.types.archive_container_settings

        out["container_settings"] = (
            aws_sdk_medialive.types.archive_container_settings.deserialize_json(
                data["containerSettings"]
            )
        )
    if "extension" in data:
        out["extension"] = data["extension"]
    if "nameModifier" in data:
        out["name_modifier"] = data["nameModifier"]
    return out
