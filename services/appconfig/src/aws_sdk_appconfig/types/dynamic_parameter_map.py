"""Generated from Smithy shape ``com.amazonaws.appconfig#DynamicParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.dynamic_parameter_key
    import aws_sdk_appconfig.types.string_with_length_between1_and2048

DynamicParameterMap: TypeAlias = dict[
    "aws_sdk_appconfig.types.dynamic_parameter_key.DynamicParameterKey",
    "aws_sdk_appconfig.types.string_with_length_between1_and2048.StringWithLengthBetween1And2048",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DynamicParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DynamicParameterMap:
    out: DynamicParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
