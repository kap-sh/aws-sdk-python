"""Generated from Smithy shape ``com.amazonaws.lakeformation#ParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.key_string
    import capo_lakeformation.types.parameters_map_value

ParametersMap: TypeAlias = dict[
    "capo_lakeformation.types.key_string.KeyString",
    "capo_lakeformation.types.parameters_map_value.ParametersMapValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ParametersMap:
    out: ParametersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
