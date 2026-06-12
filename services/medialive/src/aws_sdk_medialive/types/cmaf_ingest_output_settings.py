"""Generated from Smithy shape ``com.amazonaws.medialive#CmafIngestOutputSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class CmafIngestOutputSettings(TypedDict):
    name_modifier: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """String concatenated to the end of the destination filename. Required for multiple outputs of the same type."""


# --- restJson1 ser/de ---
def serialize_json(value: CmafIngestOutputSettings) -> dict:
    out: dict = {}
    if "name_modifier" in value:
        out["nameModifier"] = value["name_modifier"]
    return out


def deserialize_json(data: dict) -> CmafIngestOutputSettings:
    out: CmafIngestOutputSettings = {}  # type: ignore[typeddict-item]
    if "nameModifier" in data:
        out["name_modifier"] = data["nameModifier"]
    return out
