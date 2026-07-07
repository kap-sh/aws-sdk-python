"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_result_filter_criteria
    import aws_sdk_glue.types.page_size
    import aws_sdk_glue.types.pagination_token


class ListDataQualityResultsRequest(TypedDict, closed=True):
    filter: NotRequired[
        "aws_sdk_glue.types.data_quality_result_filter_criteria.DataQualityResultFilterCriteria"
    ]
    """<p>The filter criteria.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A paginated token to offset the results.</p>"""
    max_results: NotRequired["aws_sdk_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityResultsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_glue.types.data_quality_result_filter_criteria

        out["Filter"] = (
            aws_sdk_glue.types.data_quality_result_filter_criteria.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityResultsRequest:
    out: ListDataQualityResultsRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import aws_sdk_glue.types.data_quality_result_filter_criteria

        out["filter"] = (
            aws_sdk_glue.types.data_quality_result_filter_criteria.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
