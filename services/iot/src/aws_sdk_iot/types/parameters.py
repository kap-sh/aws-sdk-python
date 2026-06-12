"""Generated from Smithy shape ``com.amazonaws.iot#Parameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.parameter
    import aws_sdk_iot.types.value

Parameters: TypeAlias = dict[
    "aws_sdk_iot.types.parameter.Parameter", "aws_sdk_iot.types.value.Value"
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
