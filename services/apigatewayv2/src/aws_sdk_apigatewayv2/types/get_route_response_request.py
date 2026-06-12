"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetRouteResponseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetRouteResponseRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    route_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The route ID.</p>"""
    route_response_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The route response ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouteResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouteResponseRequest:
    out: GetRouteResponseRequest = {}  # type: ignore[typeddict-item]
    return out
