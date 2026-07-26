"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListFulfillmentOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.next_token
    import capo_marketplace_discovery.types.product_id


class ListFulfillmentOptionsInput(TypedDict, closed=True):
    product_id: "capo_marketplace_discovery.types.product_id.ProductId"
    """<p>The unique identifier of the product for which to list fulfillment options.</p>"""
    max_results: "int"
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>"""
    next_token: NotRequired["capo_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFulfillmentOptionsInput) -> dict:
    out: dict = {}
    out["productId"] = value["product_id"]
    out["maxResults"] = value.get("max_results", 25)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFulfillmentOptionsInput:
    out: ListFulfillmentOptionsInput = {}  # type: ignore[typeddict-item]
    if "productId" in data:
        out["product_id"] = data["productId"]
    else:
        raise DeserializationError("ListFulfillmentOptionsInput.product_id required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 25
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
