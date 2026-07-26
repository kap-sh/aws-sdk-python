"""Generated from Smithy shape ``com.amazonaws.greengrass#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.__string

Tags: TypeAlias = dict[
    "capo_greengrass.types.__string.__string", "capo_greengrass.types.__string.__string"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        out[key] = value
    return out
