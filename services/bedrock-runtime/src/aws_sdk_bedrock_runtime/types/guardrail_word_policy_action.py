"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailWordPolicyAction``."""

from typing import Literal, TypeAlias, cast

GuardrailWordPolicyAction: TypeAlias = Literal[
    "BLOCKED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailWordPolicyAction:
    return cast(GuardrailWordPolicyAction, data)
