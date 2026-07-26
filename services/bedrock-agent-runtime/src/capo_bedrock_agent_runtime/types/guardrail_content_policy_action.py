"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailContentPolicyAction``."""

from typing import Literal, TypeAlias, cast

GuardrailContentPolicyAction: TypeAlias = Literal["BLOCKED",]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentPolicyAction:
    return cast(GuardrailContentPolicyAction, data)
