"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Presets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.preset

Presets: TypeAlias = list["capo_elastic_transcoder.types.preset.Preset"]


# --- restJson1 ser/de ---
def serialize_json(value: Presets) -> list:
    import capo_elastic_transcoder.types.preset

    out: list = []
    for item in value:
        out.append(capo_elastic_transcoder.types.preset.serialize_json(item))
    return out


def deserialize_json(data: list) -> Presets:
    import capo_elastic_transcoder.types.preset

    out: Presets = []
    for item in data:
        out.append(capo_elastic_transcoder.types.preset.deserialize_json(item))
    return out
