"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfRoute``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.route

__listOfRoute: TypeAlias = list["aws_sdk_apigatewayv2.types.route.Route"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRoute) -> list:
    import aws_sdk_apigatewayv2.types.route

    out: list = []
    for item in value:
        out.append(aws_sdk_apigatewayv2.types.route.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRoute:
    import aws_sdk_apigatewayv2.types.route

    out: __listOfRoute = []
    for item in data:
        out.append(aws_sdk_apigatewayv2.types.route.deserialize_json(item))
    return out
