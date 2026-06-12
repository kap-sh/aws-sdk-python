"""Generated from Smithy shape ``com.amazonaws.securityhub#ParameterDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.parameter_definition

ParameterDefinitions: TypeAlias = dict[
    "aws_sdk_securityhub.types.non_empty_string.NonEmptyString",
    "aws_sdk_securityhub.types.parameter_definition.ParameterDefinition",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ParameterDefinitions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_securityhub.types.parameter_definition

        out[key] = aws_sdk_securityhub.types.parameter_definition.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ParameterDefinitions:
    out: ParameterDefinitions = {}
    for key, value in data.items():
        import aws_sdk_securityhub.types.parameter_definition

        out[key] = aws_sdk_securityhub.types.parameter_definition.deserialize_json(
            value
        )
    return out
