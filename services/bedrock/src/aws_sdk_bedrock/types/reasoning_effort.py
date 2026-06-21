"""Generated from Smithy shape ``com.amazonaws.bedrock#ReasoningEffort``."""

from typing import Literal, TypeAlias, cast

ReasoningEffort: TypeAlias = Literal[
    "low",
    "medium",
    "high",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReasoningEffort) -> str:
    return value


def deserialize_json(data: str) -> ReasoningEffort:
    return cast(ReasoningEffort, data)
