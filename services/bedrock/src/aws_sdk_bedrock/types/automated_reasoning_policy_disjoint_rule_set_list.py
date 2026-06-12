"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDisjointRuleSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set

AutomatedReasoningPolicyDisjointRuleSetList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set.AutomatedReasoningPolicyDisjointRuleSet"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDisjointRuleSetList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyDisjointRuleSetList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set

    out: AutomatedReasoningPolicyDisjointRuleSetList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_disjoint_rule_set.deserialize_json(
                item
            )
        )
    return out
