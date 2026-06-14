"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ListRoutingRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.max_results


class ListRoutingRulesRequest(TypedDict):
    domain_name: "aws_sdk_apigatewayv2.types.__string.__string"
    """<p>The domain name.</p>"""
    domain_name_id: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The domain name ID.</p>"""
    max_results: NotRequired["aws_sdk_apigatewayv2.types.max_results.MaxResults"]
    """<p>The maximum number of elements to be returned for this resource.</p>"""
    next_token: NotRequired["aws_sdk_apigatewayv2.types.__string.__string"]
    """<p>The next page of elements from this collection. Not valid for the last element of the collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoutingRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRoutingRulesRequest:
    out: ListRoutingRulesRequest = {}  # type: ignore[typeddict-item]
    return out
