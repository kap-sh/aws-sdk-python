"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfRouteResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.route_response

__listOfRouteResponse: TypeAlias = list[
    "aws_sdk_apigatewayv2.types.route_response.RouteResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRouteResponse) -> list:
    import aws_sdk_apigatewayv2.types.route_response

    out: list = []
    for item in value:
        out.append(aws_sdk_apigatewayv2.types.route_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRouteResponse:
    import aws_sdk_apigatewayv2.types.route_response

    out: __listOfRouteResponse = []
    for item in data:
        out.append(aws_sdk_apigatewayv2.types.route_response.deserialize_json(item))
    return out
