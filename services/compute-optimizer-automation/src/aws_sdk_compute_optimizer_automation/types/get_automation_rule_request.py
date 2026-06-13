"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#GetAutomationRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.rule_arn


class GetAutomationRuleRequest(TypedDict):
    rule_arn: "aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn"
    """<p> The ARN of the rule to retrieve. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutomationRuleRequest) -> dict:
    out: dict = {}
    out["ruleArn"] = value["rule_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutomationRuleRequest:
    out: GetAutomationRuleRequest = {}  # type: ignore[typeddict-item]
    if "ruleArn" in data:
        out["rule_arn"] = data["ruleArn"]
    else:
        raise DeserializationError("GetAutomationRuleRequest.rule_arn required")
    return out
