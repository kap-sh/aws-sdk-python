"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeleteRouteResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class DeleteRouteResponseRequest(TypedDict, closed=True):
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    route_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The route ID.</p>"""
    route_response_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The route response ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouteResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRouteResponseRequest:
    out: DeleteRouteResponseRequest = {}  # type: ignore[typeddict-item]
    return out
