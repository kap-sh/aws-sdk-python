"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateComplianceDetailsByConfigRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregate_evaluation_result_list
    import aws_sdk_config_service.types.next_token


class GetAggregateComplianceDetailsByConfigRuleResponse(TypedDict, closed=True):
    aggregate_evaluation_results: NotRequired[
        "aws_sdk_config_service.types.aggregate_evaluation_result_list.AggregateEvaluationResultList"
    ]
    """<p>Returns an AggregateEvaluationResults object.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetAggregateComplianceDetailsByConfigRuleResponse,
) -> dict:
    out: dict = {}
    if "aggregate_evaluation_results" in value:
        import aws_sdk_config_service.types.aggregate_evaluation_result_list

        out["AggregateEvaluationResults"] = (
            aws_sdk_config_service.types.aggregate_evaluation_result_list.serialize_aws_json_1_1(
                value["aggregate_evaluation_results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetAggregateComplianceDetailsByConfigRuleResponse:
    out: GetAggregateComplianceDetailsByConfigRuleResponse = {}  # type: ignore[typeddict-item]
    if "AggregateEvaluationResults" in data:
        import aws_sdk_config_service.types.aggregate_evaluation_result_list

        out["aggregate_evaluation_results"] = (
            aws_sdk_config_service.types.aggregate_evaluation_result_list.deserialize_aws_json_1_1(
                data["AggregateEvaluationResults"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
