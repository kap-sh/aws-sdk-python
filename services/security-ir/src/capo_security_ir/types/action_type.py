"""Generated from Smithy shape ``com.amazonaws.securityir#ActionType``."""

from typing import Literal, TypeAlias, cast

ActionType: TypeAlias = Literal[
    "Evidence",
    "Investigation",
    "Summarization",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionType) -> str:
    return value


def deserialize_json(data: str) -> ActionType:
    return cast(ActionType, data)
