"""Generated from Smithy shape ``com.amazonaws.neptunegraph#DocumentValuedMap``."""

from typing import TypeAlias

DocumentValuedMap: TypeAlias = dict["str", "object"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DocumentValuedMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DocumentValuedMap:
    out: DocumentValuedMap = {}
    for key, value in data.items():
        out[key] = value
    return out
