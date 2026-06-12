"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#StageVariablesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.string_with_length_between0_and2048

StageVariablesMap: TypeAlias = dict[
    "aws_sdk_apigatewayv2.types.__string.__string",
    "aws_sdk_apigatewayv2.types.string_with_length_between0_and2048.StringWithLengthBetween0And2048",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StageVariablesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> StageVariablesMap:
    out: StageVariablesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
