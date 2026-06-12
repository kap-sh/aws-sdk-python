"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDisjointedRuleIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id

AutomatedReasoningPolicyDisjointedRuleIdList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule_id.AutomatedReasoningPolicyDefinitionRuleId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDisjointedRuleIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutomatedReasoningPolicyDisjointedRuleIdList:
    return list(data)
