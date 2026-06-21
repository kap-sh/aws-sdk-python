"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicAction``."""

from typing import Literal, TypeAlias, cast

GuardrailTopicAction: TypeAlias = Literal[
    "BLOCK",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTopicAction:
    return cast(GuardrailTopicAction, data)
