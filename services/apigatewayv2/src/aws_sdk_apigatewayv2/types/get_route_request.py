"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetRouteRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string


class GetRouteRequest(TypedDict):
    api_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    route_id: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The route ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouteRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouteRequest:
    out: GetRouteRequest = {}  # type: ignore[typeddict-item]
    return out
