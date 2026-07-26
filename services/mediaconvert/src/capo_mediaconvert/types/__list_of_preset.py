"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfPreset``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.preset

__listOfPreset: TypeAlias = list["capo_mediaconvert.types.preset.Preset"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPreset) -> list:
    import capo_mediaconvert.types.preset

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.preset.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPreset:
    import capo_mediaconvert.types.preset

    out: __listOfPreset = []
    for item in data:
        out.append(capo_mediaconvert.types.preset.deserialize_json(item))
    return out
