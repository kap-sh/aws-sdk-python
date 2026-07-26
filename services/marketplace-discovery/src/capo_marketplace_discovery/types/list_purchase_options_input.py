"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListPurchaseOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.max_results
    import capo_marketplace_discovery.types.next_token
    import capo_marketplace_discovery.types.purchase_option_filter_list


class ListPurchaseOptionsInput(TypedDict, closed=True):
    filters: NotRequired[
        "capo_marketplace_discovery.types.purchase_option_filter_list.PurchaseOptionFilterList"
    ]
    """<p>Filters to narrow the results. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.</p>"""
    max_results: "capo_marketplace_discovery.types.max_results.MaxResults"
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>"""
    next_token: NotRequired["capo_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPurchaseOptionsInput) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_marketplace_discovery.types.purchase_option_filter_list

        out["filters"] = (
            capo_marketplace_discovery.types.purchase_option_filter_list.serialize_json(
                value["filters"]
            )
        )
    out["maxResults"] = value.get("max_results", 25)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPurchaseOptionsInput:
    out: ListPurchaseOptionsInput = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_marketplace_discovery.types.purchase_option_filter_list

        out["filters"] = (
            capo_marketplace_discovery.types.purchase_option_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 25
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
