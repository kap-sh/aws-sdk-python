"""Generated from Smithy shape ``com.amazonaws.finspacedata#SourceParams``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace_data.types.string_map_key
    import capo_finspace_data.types.string_map_value

SourceParams: TypeAlias = dict[
    "capo_finspace_data.types.string_map_key.StringMapKey",
    "capo_finspace_data.types.string_map_value.StringMapValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SourceParams) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SourceParams:
    out: SourceParams = {}
    for key, value in data.items():
        out[key] = value
    return out
