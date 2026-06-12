"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityRulesetEvaluationRunsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_ruleset_evaluation_run_filter
    import aws_sdk_glue.types.page_size
    import aws_sdk_glue.types.pagination_token


class ListDataQualityRulesetEvaluationRunsRequest(TypedDict):
    filter: NotRequired[
        "aws_sdk_glue.types.data_quality_ruleset_evaluation_run_filter.DataQualityRulesetEvaluationRunFilter"
    ]
    """<p>The filter criteria.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A paginated token to offset the results.</p>"""
    max_results: NotRequired["aws_sdk_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityRulesetEvaluationRunsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_glue.types.data_quality_ruleset_evaluation_run_filter

        out["Filter"] = (
            aws_sdk_glue.types.data_quality_ruleset_evaluation_run_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityRulesetEvaluationRunsRequest:
    out: ListDataQualityRulesetEvaluationRunsRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import aws_sdk_glue.types.data_quality_ruleset_evaluation_run_filter

        out["filter"] = (
            aws_sdk_glue.types.data_quality_ruleset_evaluation_run_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
