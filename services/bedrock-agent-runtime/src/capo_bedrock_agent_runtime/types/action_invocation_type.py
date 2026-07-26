"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ActionInvocationType``."""

from typing import Literal, TypeAlias, cast

ActionInvocationType: TypeAlias = Literal[
    "RESULT",
    "USER_CONFIRMATION",
    "USER_CONFIRMATION_AND_RESULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionInvocationType) -> str:
    return value


def deserialize_json(data: str) -> ActionInvocationType:
    return cast(ActionInvocationType, data)
