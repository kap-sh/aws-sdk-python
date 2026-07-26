"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContextualGroundingPolicyAction``."""

from typing import Literal, TypeAlias, cast

GuardrailContextualGroundingPolicyAction: TypeAlias = Literal[
    "BLOCKED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContextualGroundingPolicyAction:
    return cast(GuardrailContextualGroundingPolicyAction, data)
