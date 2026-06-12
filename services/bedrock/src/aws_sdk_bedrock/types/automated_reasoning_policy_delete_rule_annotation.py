"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDeleteRuleAnnotation``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id


class AutomatedReasoningPolicyDeleteRuleAnnotation(TypedDict):
    rule_id: "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId"
    """<p>The unique identifier of the rule to delete from the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDeleteRuleAnnotation) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDeleteRuleAnnotation:
    out: AutomatedReasoningPolicyDeleteRuleAnnotation = {}  # type: ignore[typeddict-item]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDeleteRuleAnnotation.rule_id required"
        )
    return out
