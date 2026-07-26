"""Generated from Smithy shape ``com.amazonaws.connect#DimensionsV2Map``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.dimensions_v2_key
    import capo_connect.types.dimensions_v2_value

DimensionsV2Map: TypeAlias = dict[
    "capo_connect.types.dimensions_v2_key.DimensionsV2Key",
    "capo_connect.types.dimensions_v2_value.DimensionsV2Value",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DimensionsV2Map) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DimensionsV2Map:
    out: DimensionsV2Map = {}
    for key, value in data.items():
        out[key] = value
    return out
