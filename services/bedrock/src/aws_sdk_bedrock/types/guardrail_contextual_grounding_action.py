"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingAction``."""

from typing import Literal, TypeAlias, cast

GuardrailContextualGroundingAction: TypeAlias = Literal[
    "BLOCK",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContextualGroundingAction:
    return cast(GuardrailContextualGroundingAction, data)
