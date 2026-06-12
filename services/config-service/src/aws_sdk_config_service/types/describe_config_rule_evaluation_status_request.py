"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigRuleEvaluationStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule_names
    import aws_sdk_config_service.types.rule_limit
    import aws_sdk_config_service.types.string


class DescribeConfigRuleEvaluationStatusRequest(TypedDict):
    config_rule_names: NotRequired[
        "aws_sdk_config_service.types.config_rule_names.ConfigRuleNames"
    ]
    """<p>The name of the Config managed rules for which you want status information. If you do not specify any names, Config returns status information for all Config managed rules that you use.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""
    limit: "aws_sdk_config_service.types.rule_limit.RuleLimit"
    """<p>The number of rule evaluation results that you want returned.</p> <p>This parameter is required if the rule limit for your account is more than the default of 1000 rules.</p> <p>For information about requesting a rule limit increase, see <a href=\"http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_config\">Config Limits</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigRuleEvaluationStatusRequest) -> dict:
    out: dict = {}
    if "config_rule_names" in value:
        import aws_sdk_config_service.types.config_rule_names

        out["ConfigRuleNames"] = (
            aws_sdk_config_service.types.config_rule_names.serialize_aws_json_1_1(
                value["config_rule_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["Limit"] = value.get("limit", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigRuleEvaluationStatusRequest:
    out: DescribeConfigRuleEvaluationStatusRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRuleNames" in data:
        import aws_sdk_config_service.types.config_rule_names

        out["config_rule_names"] = (
            aws_sdk_config_service.types.config_rule_names.deserialize_aws_json_1_1(
                data["ConfigRuleNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    return out
