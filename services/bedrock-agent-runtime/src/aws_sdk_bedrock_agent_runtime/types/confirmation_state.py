"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ConfirmationState``."""

from typing import Literal, TypeAlias, cast

ConfirmationState: TypeAlias = Literal[
    "CONFIRM",
    "DENY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfirmationState) -> str:
    return value


def deserialize_json(data: str) -> ConfirmationState:
    return cast(ConfirmationState, data)
