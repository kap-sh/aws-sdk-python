"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StringMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.string_map_key
    import capo_migrationhuborchestrator.types.string_map_value

StringMap: TypeAlias = dict[
    "capo_migrationhuborchestrator.types.string_map_key.StringMapKey",
    "capo_migrationhuborchestrator.types.string_map_value.StringMapValue",
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
