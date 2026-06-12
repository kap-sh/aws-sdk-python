"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule

AutomatedReasoningPolicyDefinitionRuleList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.AutomatedReasoningPolicyDefinitionRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionRuleList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyDefinitionRuleList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule

    out: AutomatedReasoningPolicyDefinitionRuleList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_definition_rule.deserialize_json(
                item
            )
        )
    return out
