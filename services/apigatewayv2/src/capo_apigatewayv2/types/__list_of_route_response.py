"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfRouteResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.route_response

__listOfRouteResponse: TypeAlias = list[
    "capo_apigatewayv2.types.route_response.RouteResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRouteResponse) -> list:
    import capo_apigatewayv2.types.route_response

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.route_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRouteResponse:
    import capo_apigatewayv2.types.route_response

    out: __listOfRouteResponse = []
    for item in data:
        out.append(capo_apigatewayv2.types.route_response.deserialize_json(item))
    return out
