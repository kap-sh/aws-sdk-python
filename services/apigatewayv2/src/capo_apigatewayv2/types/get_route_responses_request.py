"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#GetRouteResponsesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string


class GetRouteResponsesRequest(TypedDict, closed=True):
    api_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The API identifier.</p>"""
    max_results: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The maximum number of elements to be returned for this resource.</p>"""
    next_token: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""
    route_id: "capo_apigatewayv2.types.__string.__string"
    """<p>The route ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouteResponsesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouteResponsesRequest:
    out: GetRouteResponsesRequest = {}  # type: ignore[typeddict-item]
    return out
