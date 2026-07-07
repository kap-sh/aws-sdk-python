"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateAutomationRuleV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class CreateAutomationRuleV2Response(TypedDict, closed=True):
    rule_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the V2 automation rule.</p>"""
    rule_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the V2 automation rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomationRuleV2Response) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> CreateAutomationRuleV2Response:
    out: CreateAutomationRuleV2Response = {}  # type: ignore[typeddict-item]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    return out
