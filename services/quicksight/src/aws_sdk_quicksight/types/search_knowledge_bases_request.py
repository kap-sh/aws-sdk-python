"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchKnowledgeBasesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.kb_aws_account_id
    import aws_sdk_quicksight.types.knowledge_base_search_filters
    import aws_sdk_quicksight.types.knowledge_base_sort_by
    import aws_sdk_quicksight.types.max_results
    import aws_sdk_quicksight.types.next_token


class SearchKnowledgeBasesRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.kb_aws_account_id.KbAwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the knowledge base.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    filters: NotRequired[
        "aws_sdk_quicksight.types.knowledge_base_search_filters.KnowledgeBaseSearchFilters"
    ]
    """<p>The filters to apply when searching knowledge bases.</p>"""
    sort_by: NotRequired[
        "aws_sdk_quicksight.types.knowledge_base_sort_by.KnowledgeBaseSortBy"
    ]
    """<p>The sort configuration for the search results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchKnowledgeBasesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_quicksight.types.knowledge_base_search_filters

        out["Filters"] = (
            aws_sdk_quicksight.types.knowledge_base_search_filters.serialize_json(
                value["filters"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_quicksight.types.knowledge_base_sort_by

        out["SortBy"] = aws_sdk_quicksight.types.knowledge_base_sort_by.serialize_json(
            value["sort_by"]
        )
    return out


def deserialize_json(data: dict) -> SearchKnowledgeBasesRequest:
    out: SearchKnowledgeBasesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filters" in data:
        import aws_sdk_quicksight.types.knowledge_base_search_filters

        out["filters"] = (
            aws_sdk_quicksight.types.knowledge_base_search_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_quicksight.types.knowledge_base_sort_by

        out["sort_by"] = (
            aws_sdk_quicksight.types.knowledge_base_sort_by.deserialize_json(
                data["SortBy"]
            )
        )
    return out
