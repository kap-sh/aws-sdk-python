"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchRelatedItemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_id
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.next_token
    import aws_sdk_connectcases.types.related_item_filter_list


class SearchRelatedItemsRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    case_id: "aws_sdk_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    filters: NotRequired[
        "aws_sdk_connectcases.types.related_item_filter_list.RelatedItemFilterList"
    ]
    """<p>The list of types of related items and their parameters to use for filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRelatedItemsRequest) -> dict:
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
    return out


def deserialize_json(data: dict) -> SearchRelatedItemsRequest:
    out: SearchRelatedItemsRequest = {}  # type: ignore[typeddict-item]
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
    return out
