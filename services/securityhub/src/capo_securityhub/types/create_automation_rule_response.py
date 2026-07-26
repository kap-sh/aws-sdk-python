"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateAutomationRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class CreateAutomationRuleResponse(TypedDict, closed=True):
    rule_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the automation rule that you created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomationRuleResponse) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    return out


def deserialize_json(data: dict) -> CreateAutomationRuleResponse:
    out: CreateAutomationRuleResponse = {}  # type: ignore[typeddict-item]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    return out
