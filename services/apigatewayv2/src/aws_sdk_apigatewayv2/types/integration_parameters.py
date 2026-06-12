"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#IntegrationParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and512

IntegrationParameters: TypeAlias = dict[
    "aws_sdk_apigatewayv2.types.__string.__string",
    "aws_sdk_apigatewayv2.types.string_with_length_between1_and512.StringWithLengthBetween1And512",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: IntegrationParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> IntegrationParameters:
    out: IntegrationParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
