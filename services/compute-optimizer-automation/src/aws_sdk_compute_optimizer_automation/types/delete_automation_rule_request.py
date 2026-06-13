"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#DeleteAutomationRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.client_token
    import aws_sdk_compute_optimizer_automation.types.rule_arn


class DeleteAutomationRuleRequest(TypedDict):
    rule_arn: "aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn"
    """<p> The ARN of the rule to delete. </p>"""
    rule_revision: "int"
    """<p> The revision number of the rule to delete. </p>"""
    client_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p> A unique identifier to ensure idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAutomationRuleRequest) -> dict:
    out: dict = {}
    out["ruleArn"] = value["rule_arn"]
    out["ruleRevision"] = value["rule_revision"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAutomationRuleRequest:
    out: DeleteAutomationRuleRequest = {}  # type: ignore[typeddict-item]
    if "ruleArn" in data:
        out["rule_arn"] = data["ruleArn"]
    else:
        raise DeserializationError("DeleteAutomationRuleRequest.rule_arn required")
    if "ruleRevision" in data:
        out["rule_revision"] = data["ruleRevision"]
    else:
        raise DeserializationError("DeleteAutomationRuleRequest.rule_revision required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
