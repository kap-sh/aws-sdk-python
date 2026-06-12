"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyConflictedRuleIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id

AutomatedReasoningPolicyConflictedRuleIdList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyConflictedRuleIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutomatedReasoningPolicyConflictedRuleIdList:
    return list(data)
