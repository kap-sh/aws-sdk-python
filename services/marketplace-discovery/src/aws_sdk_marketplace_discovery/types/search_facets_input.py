"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchFacetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.facet_type_list
    import aws_sdk_marketplace_discovery.types.next_token
    import aws_sdk_marketplace_discovery.types.search_filter_list
    import aws_sdk_marketplace_discovery.types.search_text


class SearchFacetsInput(TypedDict, closed=True):
    search_text: NotRequired[
        "aws_sdk_marketplace_discovery.types.search_text.SearchText"
    ]
    """<p>The search query text to filter listings before retrieving facets.</p>"""
    filters: NotRequired[
        "aws_sdk_marketplace_discovery.types.search_filter_list.SearchFilterList"
    ]
    """<p>Filters to apply before retrieving facets. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.</p>"""
    facet_types: NotRequired[
        "aws_sdk_marketplace_discovery.types.facet_type_list.FacetTypeList"
    ]
    """<p>A list of specific facet types to retrieve. If empty or null, all available facets are returned.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFacetsInput) -> dict:
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
    if "facet_types" in value:
        import aws_sdk_marketplace_discovery.types.facet_type_list

        out["facetTypes"] = (
            aws_sdk_marketplace_discovery.types.facet_type_list.serialize_json(
                value["facet_types"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchFacetsInput:
    out: SearchFacetsInput = {}  # type: ignore[typeddict-item]
    if "searchText" in data:
        out["search_text"] = data["searchText"]
    if "filters" in data:
        import aws_sdk_marketplace_discovery.types.search_filter_list

        out["filters"] = (
            aws_sdk_marketplace_discovery.types.search_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if "facetTypes" in data:
        import aws_sdk_marketplace_discovery.types.facet_type_list

        out["facet_types"] = (
            aws_sdk_marketplace_discovery.types.facet_type_list.deserialize_json(
                data["facetTypes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
