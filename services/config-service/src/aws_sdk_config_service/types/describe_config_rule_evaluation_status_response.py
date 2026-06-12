"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigRuleEvaluationStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule_evaluation_status_list
    import aws_sdk_config_service.types.string


class DescribeConfigRuleEvaluationStatusResponse(TypedDict):
    config_rules_evaluation_status: NotRequired[
        "aws_sdk_config_service.types.config_rule_evaluation_status_list.ConfigRuleEvaluationStatusList"
    ]
    """<p>Status information about your Config managed rules.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The string that you use in a subsequent request to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigRuleEvaluationStatusResponse) -> dict:
    out: dict = {}
    if "config_rules_evaluation_status" in value:
        import aws_sdk_config_service.types.config_rule_evaluation_status_list

        out["ConfigRulesEvaluationStatus"] = (
            aws_sdk_config_service.types.config_rule_evaluation_status_list.serialize_aws_json_1_1(
                value["config_rules_evaluation_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigRuleEvaluationStatusResponse:
    out: DescribeConfigRuleEvaluationStatusResponse = {}  # type: ignore[typeddict-item]
    if "ConfigRulesEvaluationStatus" in data:
        import aws_sdk_config_service.types.config_rule_evaluation_status_list

        out["config_rules_evaluation_status"] = (
            aws_sdk_config_service.types.config_rule_evaluation_status_list.deserialize_aws_json_1_1(
                data["ConfigRulesEvaluationStatus"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
