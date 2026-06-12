"""Generated from Smithy shape ``com.amazonaws.appconfig#ParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.extension_or_parameter_name
    import aws_sdk_appconfig.types.parameter

ParameterMap: TypeAlias = dict[
    "aws_sdk_appconfig.types.extension_or_parameter_name.ExtensionOrParameterName",
    "aws_sdk_appconfig.types.parameter.Parameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_appconfig.types.parameter

        out[key] = aws_sdk_appconfig.types.parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ParameterMap:
    out: ParameterMap = {}
    for key, value in data.items():
        import aws_sdk_appconfig.types.parameter

        out[key] = aws_sdk_appconfig.types.parameter.deserialize_json(value)
    return out
