"""Generated from Smithy shape ``com.amazonaws.configservice#GetConformancePackComplianceDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_name
    import aws_sdk_config_service.types.conformance_pack_rule_evaluation_results_list
    import aws_sdk_config_service.types.next_token


class GetConformancePackComplianceDetailsResponse(TypedDict, closed=True):
    conformance_pack_name: (
        "aws_sdk_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>Name of the conformance pack.</p>"""
    conformance_pack_rule_evaluation_results: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_rule_evaluation_results_list.ConformancePackRuleEvaluationResultsList"
    ]
    """<p>Returns a list of <code>ConformancePackEvaluationResult</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConformancePackComplianceDetailsResponse) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    if "conformance_pack_rule_evaluation_results" in value:
        import aws_sdk_config_service.types.conformance_pack_rule_evaluation_results_list

        out["ConformancePackRuleEvaluationResults"] = (
            aws_sdk_config_service.types.conformance_pack_rule_evaluation_results_list.serialize_aws_json_1_1(
                value["conformance_pack_rule_evaluation_results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConformancePackComplianceDetailsResponse:
    out: GetConformancePackComplianceDetailsResponse = {}  # type: ignore[typeddict-item]
    if "ConformancePackName" in data:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        raise DeserializationError(
            "GetConformancePackComplianceDetailsResponse.conformance_pack_name required"
        )
    if "ConformancePackRuleEvaluationResults" in data:
        import aws_sdk_config_service.types.conformance_pack_rule_evaluation_results_list

        out["conformance_pack_rule_evaluation_results"] = (
            aws_sdk_config_service.types.conformance_pack_rule_evaluation_results_list.deserialize_aws_json_1_1(
                data["ConformancePackRuleEvaluationResults"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
