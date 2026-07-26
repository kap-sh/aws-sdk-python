"""Generated from Smithy shape ``com.amazonaws.datazone#Parameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.parameter_key
    import capo_datazone.types.parameter_value

Parameters: TypeAlias = dict[
    "capo_datazone.types.parameter_key.ParameterKey",
    "capo_datazone.types.parameter_value.ParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Parameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Parameters:
    out: Parameters = {}
    for key, value in data.items():
        out[key] = value
    return out
