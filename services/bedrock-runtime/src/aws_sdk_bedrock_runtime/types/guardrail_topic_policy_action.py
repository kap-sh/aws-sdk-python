"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTopicPolicyAction``."""

from typing import Literal, TypeAlias, cast

GuardrailTopicPolicyAction: TypeAlias = Literal[
    "BLOCKED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTopicPolicyAction:
    return cast(GuardrailTopicPolicyAction, data)
