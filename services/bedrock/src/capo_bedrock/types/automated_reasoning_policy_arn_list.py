"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn

AutomatedReasoningPolicyArnList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutomatedReasoningPolicyArnList:
    return list(data)
