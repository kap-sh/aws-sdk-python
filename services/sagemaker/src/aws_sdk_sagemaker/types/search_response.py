"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.search_results_list
    import aws_sdk_sagemaker.types.total_hits


class SearchResponse(TypedDict, closed=True):
    results: NotRequired[
        "aws_sdk_sagemaker.types.search_results_list.SearchResultsList"
    ]
    """<p>A list of <code>SearchRecord</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>Search</code> request was truncated, the response includes a NextToken. To retrieve the next set of results, use the token in the next request.</p>"""
    total_hits: NotRequired["aws_sdk_sagemaker.types.total_hits.TotalHits"]
    """<p>The total number of matching results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchResponse) -> dict:
    out: dict = {}
    if "results" in value:
        import aws_sdk_sagemaker.types.search_results_list

        out["Results"] = (
            aws_sdk_sagemaker.types.search_results_list.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "total_hits" in value:
        import aws_sdk_sagemaker.types.total_hits

        out["TotalHits"] = aws_sdk_sagemaker.types.total_hits.serialize_aws_json_1_1(
            value["total_hits"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchResponse:
    out: SearchResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_sagemaker.types.search_results_list

        out["results"] = (
            aws_sdk_sagemaker.types.search_results_list.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TotalHits" in data:
        import aws_sdk_sagemaker.types.total_hits

        out["total_hits"] = aws_sdk_sagemaker.types.total_hits.deserialize_aws_json_1_1(
            data["TotalHits"]
        )
    return out
