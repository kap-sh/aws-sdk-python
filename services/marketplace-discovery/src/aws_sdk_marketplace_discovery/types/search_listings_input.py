"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchListingsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.max_results
    import aws_sdk_marketplace_discovery.types.next_token
    import aws_sdk_marketplace_discovery.types.search_filter_list
    import aws_sdk_marketplace_discovery.types.search_listings_sort_by
    import aws_sdk_marketplace_discovery.types.search_listings_sort_order
    import aws_sdk_marketplace_discovery.types.search_text


class SearchListingsInput(TypedDict):
    search_text: NotRequired[
        "aws_sdk_marketplace_discovery.types.search_text.SearchText"
    ]
    """<p>The search query text to find relevant listings.</p>"""
    filters: NotRequired[
        "aws_sdk_marketplace_discovery.types.search_filter_list.SearchFilterList"
    ]
    """<p>Filters to narrow search results. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.</p>"""
    max_results: "aws_sdk_marketplace_discovery.types.max_results.MaxResults"
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to get more results.</p>"""
    sort_by: "aws_sdk_marketplace_discovery.types.search_listings_sort_by.SearchListingsSortBy"
    """<p>The field to sort results by. Valid values are <code>RELEVANCE</code> and <code>AVERAGE_CUSTOMER_RATING</code>.</p>"""
    sort_order: "aws_sdk_marketplace_discovery.types.search_listings_sort_order.SearchListingsSortOrder"
    """<p>The sort direction. Valid values are <code>DESCENDING</code> and <code>ASCENDING</code>.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchListingsInput) -> dict:
    out: dict = {}
    if "search_text" in value:
        out["searchText"] = value["search_text"]
    if "filters" in value:
        import aws_sdk_marketplace_discovery.types.search_filter_list

        out["filters"] = (
            aws_sdk_marketplace_discovery.types.search_filter_list.serialize_json(
                value["filters"]
            )
        )
    out["maxResults"] = value.get("max_results", 25)
    import aws_sdk_marketplace_discovery.types.search_listings_sort_by

    out["sortBy"] = (
        aws_sdk_marketplace_discovery.types.search_listings_sort_by.serialize_json(
            value.get("sort_by", "RELEVANCE")
        )
    )
    import aws_sdk_marketplace_discovery.types.search_listings_sort_order

    out["sortOrder"] = (
        aws_sdk_marketplace_discovery.types.search_listings_sort_order.serialize_json(
            value.get("sort_order", "DESCENDING")
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchListingsInput:
    out: SearchListingsInput = {}  # type: ignore[typeddict-item]
    if "searchText" in data:
        out["search_text"] = data["searchText"]
    if "filters" in data:
        import aws_sdk_marketplace_discovery.types.search_filter_list

        out["filters"] = (
            aws_sdk_marketplace_discovery.types.search_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 25
    if "sortBy" in data:
        import aws_sdk_marketplace_discovery.types.search_listings_sort_by

        out["sort_by"] = (
            aws_sdk_marketplace_discovery.types.search_listings_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    else:
        out["sort_by"] = "RELEVANCE"
    if "sortOrder" in data:
        import aws_sdk_marketplace_discovery.types.search_listings_sort_order

        out["sort_order"] = (
            aws_sdk_marketplace_discovery.types.search_listings_sort_order.deserialize_json(
                data["sortOrder"]
            )
        )
    else:
        out["sort_order"] = "DESCENDING"
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
