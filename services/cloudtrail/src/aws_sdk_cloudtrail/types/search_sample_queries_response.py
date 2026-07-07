"""Generated from Smithy shape ``com.amazonaws.cloudtrail#SearchSampleQueriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.pagination_token
    import aws_sdk_cloudtrail.types.search_sample_queries_search_results


class SearchSampleQueriesResponse(TypedDict, closed=True):
    search_results: NotRequired[
        "aws_sdk_cloudtrail.types.search_sample_queries_search_results.SearchSampleQueriesSearchResults"
    ]
    """<p> A list of objects containing the search results ordered from most relevant to least relevant. </p>"""
    next_token: NotRequired["aws_sdk_cloudtrail.types.pagination_token.PaginationToken"]
    """<p> A token you can use to get the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchSampleQueriesResponse) -> dict:
    out: dict = {}
    if "search_results" in value:
        import aws_sdk_cloudtrail.types.search_sample_queries_search_results

        out["SearchResults"] = (
            aws_sdk_cloudtrail.types.search_sample_queries_search_results.serialize_aws_json_1_1(
                value["search_results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchSampleQueriesResponse:
    out: SearchSampleQueriesResponse = {}  # type: ignore[typeddict-item]
    if "SearchResults" in data:
        import aws_sdk_cloudtrail.types.search_sample_queries_search_results

        out["search_results"] = (
            aws_sdk_cloudtrail.types.search_sample_queries_search_results.deserialize_aws_json_1_1(
                data["SearchResults"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
