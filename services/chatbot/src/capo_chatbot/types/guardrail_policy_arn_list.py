"""Generated from Smithy shape ``com.amazonaws.chatbot#GuardrailPolicyArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chatbot.types.guardrail_policy_arn

GuardrailPolicyArnList: TypeAlias = list[
    "capo_chatbot.types.guardrail_policy_arn.GuardrailPolicyArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPolicyArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> GuardrailPolicyArnList:
    return list(data)
