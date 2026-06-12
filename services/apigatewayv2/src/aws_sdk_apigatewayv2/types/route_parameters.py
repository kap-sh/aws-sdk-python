"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RouteParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.parameter_constraints

RouteParameters: TypeAlias = dict[
    "aws_sdk_apigatewayv2.types.__string.__string",
    "aws_sdk_apigatewayv2.types.parameter_constraints.ParameterConstraints",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RouteParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_apigatewayv2.types.parameter_constraints

        out[key] = aws_sdk_apigatewayv2.types.parameter_constraints.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> RouteParameters:
    out: RouteParameters = {}
    for key, value in data.items():
        import aws_sdk_apigatewayv2.types.parameter_constraints

        out[key] = aws_sdk_apigatewayv2.types.parameter_constraints.deserialize_json(
            value
        )
    return out
