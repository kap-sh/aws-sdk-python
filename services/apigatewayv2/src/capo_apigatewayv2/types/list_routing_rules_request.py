"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ListRoutingRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.max_results


class ListRoutingRulesRequest(TypedDict, closed=True):
    domain_name: "capo_apigatewayv2.types.__string.__string"
    """<p>The domain name.</p>"""
    domain_name_id: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The domain name ID.</p>"""
    max_results: NotRequired["capo_apigatewayv2.types.max_results.MaxResults"]
    """<p>The maximum number of elements to be returned for this resource.</p>"""
    next_token: NotRequired["capo_apigatewayv2.types.__string.__string"]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoutingRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRoutingRulesRequest:
    out: ListRoutingRulesRequest = {}  # type: ignore[typeddict-item]
    return out
