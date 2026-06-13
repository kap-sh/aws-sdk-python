"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchAllRelatedItemsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.next_token
    import aws_sdk_connectcases.types.related_item_filter_list
    import aws_sdk_connectcases.types.search_all_related_items_sort_list


class SearchAllRelatedItemsRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    filters: NotRequired[
        "aws_sdk_connectcases.types.related_item_filter_list.RelatedItemFilterList"
    ]
    """<p>The list of types of related items and their parameters to use for filtering. The filters work as an OR condition: caller gets back related items that match any of the specified filter types.</p>"""
    sorts: NotRequired[
        "aws_sdk_connectcases.types.search_all_related_items_sort_list.SearchAllRelatedItemsSortList"
    ]
    """<p>A structured set of sort terms to specify the order in which related items should be returned. Supports sorting by association time or case ID. The sorts work in the order specified: first sort term takes precedence over subsequent terms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAllRelatedItemsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_connectcases.types.related_item_filter_list

        out["filters"] = (
            aws_sdk_connectcases.types.related_item_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "sorts" in value:
        import aws_sdk_connectcases.types.search_all_related_items_sort_list

        out["sorts"] = (
            aws_sdk_connectcases.types.search_all_related_items_sort_list.serialize_json(
                value["sorts"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchAllRelatedItemsRequest:
    out: SearchAllRelatedItemsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "filters" in data:
        import aws_sdk_connectcases.types.related_item_filter_list

        out["filters"] = (
            aws_sdk_connectcases.types.related_item_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if "sorts" in data:
        import aws_sdk_connectcases.types.search_all_related_items_sort_list

        out["sorts"] = (
            aws_sdk_connectcases.types.search_all_related_items_sort_list.deserialize_json(
                data["sorts"]
            )
        )
    return out
