"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptState``."""

from typing import Literal, TypeAlias, cast

PromptState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptState) -> str:
    return value


def deserialize_json(data: str) -> PromptState:
    return cast(PromptState, data)
