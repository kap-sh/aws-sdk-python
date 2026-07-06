"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityRulesetEvaluationRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_ruleset_evaluation_run_list
    import aws_sdk_glue.types.pagination_token


class ListDataQualityRulesetEvaluationRunsResponse(TypedDict, closed=True):
    runs: NotRequired[
        "aws_sdk_glue.types.data_quality_ruleset_evaluation_run_list.DataQualityRulesetEvaluationRunList"
    ]
    """<p>A list of <code>DataQualityRulesetEvaluationRunDescription</code> objects representing data quality ruleset runs.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token, if more results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityRulesetEvaluationRunsResponse) -> dict:
    out: dict = {}
    if "runs" in value:
        import aws_sdk_glue.types.data_quality_ruleset_evaluation_run_list

        out["Runs"] = (
            aws_sdk_glue.types.data_quality_ruleset_evaluation_run_list.serialize_aws_json_1_1(
                value["runs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListDataQualityRulesetEvaluationRunsResponse:
    out: ListDataQualityRulesetEvaluationRunsResponse = {}  # type: ignore[typeddict-item]
    if "Runs" in data:
        import aws_sdk_glue.types.data_quality_ruleset_evaluation_run_list

        out["runs"] = (
            aws_sdk_glue.types.data_quality_ruleset_evaluation_run_list.deserialize_aws_json_1_1(
                data["Runs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
