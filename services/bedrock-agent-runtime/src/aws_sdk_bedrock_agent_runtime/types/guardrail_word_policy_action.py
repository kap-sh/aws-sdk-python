"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailWordPolicyAction``."""

from typing import Literal, TypeAlias, cast

GuardrailWordPolicyAction: TypeAlias = Literal["BLOCKED",]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailWordPolicyAction:
    return cast(GuardrailWordPolicyAction, data)
