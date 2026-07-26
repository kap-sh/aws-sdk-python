"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityRuleRecommendationRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_quality_rule_recommendation_run_filter
    import capo_glue.types.page_size
    import capo_glue.types.pagination_token


class ListDataQualityRuleRecommendationRunsRequest(TypedDict, closed=True):
    filter: NotRequired[
        "capo_glue.types.data_quality_rule_recommendation_run_filter.DataQualityRuleRecommendationRunFilter"
    ]
    """<p>The filter criteria.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A paginated token to offset the results.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityRuleRecommendationRunsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_glue.types.data_quality_rule_recommendation_run_filter

        out["Filter"] = (
            capo_glue.types.data_quality_rule_recommendation_run_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListDataQualityRuleRecommendationRunsRequest:
    out: ListDataQualityRuleRecommendationRunsRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import capo_glue.types.data_quality_rule_recommendation_run_filter

        out["filter"] = (
            capo_glue.types.data_quality_rule_recommendation_run_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
