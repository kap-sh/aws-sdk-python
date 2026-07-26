"""Generated from Smithy shape ``com.amazonaws.iot#ParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.parameter_key
    import capo_iot.types.parameter_value

ParameterMap: TypeAlias = dict[
    "capo_iot.types.parameter_key.ParameterKey",
    "capo_iot.types.parameter_value.ParameterValue",
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
