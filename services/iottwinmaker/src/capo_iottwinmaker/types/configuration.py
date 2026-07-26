"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Configuration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.value

Configuration: TypeAlias = dict[
    "capo_iottwinmaker.types.name.Name", "capo_iottwinmaker.types.value.Value"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Configuration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Configuration:
    out: Configuration = {}
    for key, value in data.items():
        out[key] = value
    return out
