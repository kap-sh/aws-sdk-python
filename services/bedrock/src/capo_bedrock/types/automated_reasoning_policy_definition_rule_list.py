"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule

AutomatedReasoningPolicyDefinitionRuleList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_definition_rule.AutomatedReasoningPolicyDefinitionRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionRuleList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_definition_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionRuleList:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule

    out: AutomatedReasoningPolicyDefinitionRuleList = []
    for item in data:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_definition_rule.deserialize_json(
                item
            )
        )
    return out
