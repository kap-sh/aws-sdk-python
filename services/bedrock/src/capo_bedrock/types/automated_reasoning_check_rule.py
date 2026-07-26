"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_id


class AutomatedReasoningCheckRule(TypedDict, closed=True):
    id: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId"
    ]
    """<p>The unique identifier of the automated reasoning rule.</p>"""
    policy_version_arn: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    ]
    """<p>The ARN of the automated reasoning policy version that contains this rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckRule) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "policy_version_arn" in value:
        out["policyVersionArn"] = value["policy_version_arn"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckRule:
    out: AutomatedReasoningCheckRule = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "policyVersionArn" in data:
        out["policy_version_arn"] = data["policyVersionArn"]
    return out
