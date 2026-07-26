"""Generated from Smithy shape ``com.amazonaws.databrew#ParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.parameter_name
    import capo_databrew.types.parameter_value

ParameterMap: TypeAlias = dict[
    "capo_databrew.types.parameter_name.ParameterName",
    "capo_databrew.types.parameter_value.ParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ParameterMap:
    out: ParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
