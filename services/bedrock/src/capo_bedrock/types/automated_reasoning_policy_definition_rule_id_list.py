"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionRuleIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule_id

AutomatedReasoningPolicyDefinitionRuleIdList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionRuleIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionRuleIdList:
    return [item for item in data if item is not None]
