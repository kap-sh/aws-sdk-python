"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetRouteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class GetRouteRequest(TypedDict, closed=True):
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    route_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The route ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouteRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouteRequest:
    out: GetRouteRequest = {}  # type: ignore[typeddict-item]
    return out
