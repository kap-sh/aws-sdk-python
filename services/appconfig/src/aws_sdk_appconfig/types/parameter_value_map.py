"""Generated from Smithy shape ``com.amazonaws.appconfig#ParameterValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.extension_or_parameter_name
    import aws_sdk_appconfig.types.string_with_length_between1_and2048

ParameterValueMap: TypeAlias = dict[
    "aws_sdk_appconfig.types.extension_or_parameter_name.ExtensionOrParameterName",
    "aws_sdk_appconfig.types.string_with_length_between1_and2048.StringWithLengthBetween1And2048",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ParameterValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ParameterValueMap:
    out: ParameterValueMap = {}
    for key, value in data.items():
        out[key] = value
    return out
