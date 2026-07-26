"""Generated from Smithy shape ``com.amazonaws.rum#DimensionKeysMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rum.types.dimension_key
    import capo_rum.types.dimension_name

DimensionKeysMap: TypeAlias = dict[
    "capo_rum.types.dimension_key.DimensionKey",
    "capo_rum.types.dimension_name.DimensionName",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DimensionKeysMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DimensionKeysMap:
    out: DimensionKeysMap = {}
    for key, value in data.items():
        out[key] = value
    return out
