"""Generated from Smithy shape ``com.amazonaws.medialive#FrameCaptureOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class FrameCaptureOutputSettings(TypedDict, closed=True):
    name_modifier: NotRequired["capo_medialive.types.__string.__string"]
    """Required if the output group contains more than one output. This modifier forms part of the output file name."""


# --- restJson1 ser/de ---
def serialize_json(value: FrameCaptureOutputSettings) -> dict:
    out: dict = {}
    if "name_modifier" in value:
        out["nameModifier"] = value["name_modifier"]
    return out


def deserialize_json(data: dict) -> FrameCaptureOutputSettings:
    out: FrameCaptureOutputSettings = {}  # type: ignore[typeddict-item]
    if "nameModifier" in data:
        out["name_modifier"] = data["nameModifier"]
    return out
