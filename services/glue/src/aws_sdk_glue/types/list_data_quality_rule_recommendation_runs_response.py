"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityRuleRecommendationRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_rule_recommendation_run_list
    import aws_sdk_glue.types.pagination_token


class ListDataQualityRuleRecommendationRunsResponse(TypedDict, closed=True):
    runs: NotRequired[
        "aws_sdk_glue.types.data_quality_rule_recommendation_run_list.DataQualityRuleRecommendationRunList"
    ]
    """<p>A list of <code>DataQualityRuleRecommendationRunDescription</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token, if more results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListDataQualityRuleRecommendationRunsResponse,
) -> dict:
    out: dict = {}
    if "runs" in value:
        import aws_sdk_glue.types.data_quality_rule_recommendation_run_list

        out["Runs"] = (
            aws_sdk_glue.types.data_quality_rule_recommendation_run_list.serialize_aws_json_1_1(
                value["runs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListDataQualityRuleRecommendationRunsResponse:
    out: ListDataQualityRuleRecommendationRunsResponse = {}  # type: ignore[typeddict-item]
    if "Runs" in data:
        import aws_sdk_glue.types.data_quality_rule_recommendation_run_list

        out["runs"] = (
            aws_sdk_glue.types.data_quality_rule_recommendation_run_list.deserialize_aws_json_1_1(
                data["Runs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
