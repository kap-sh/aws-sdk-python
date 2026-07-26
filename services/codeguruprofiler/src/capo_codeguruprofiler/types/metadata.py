"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Metadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.metadata_field

Metadata: TypeAlias = dict[
    "capo_codeguruprofiler.types.metadata_field.MetadataField", "str"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Metadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Metadata:
    out: Metadata = {}
    for key, value in data.items():
        out[key] = value
    return out
