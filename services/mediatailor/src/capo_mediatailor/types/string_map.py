"""Generated from Smithy shape ``com.amazonaws.mediatailor#StringMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.__string

StringMap: TypeAlias = dict[
    "capo_mediatailor.types.__string.__string",
    "capo_mediatailor.types.__string.__string",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StringMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> StringMap:
    out: StringMap = {}
    for key, value in data.items():
        out[key] = value
    return out
