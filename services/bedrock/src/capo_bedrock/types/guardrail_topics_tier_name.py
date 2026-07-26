"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicsTierName``."""

from typing import Literal, TypeAlias, cast

GuardrailTopicsTierName: TypeAlias = Literal[
    "CLASSIC",
    "STANDARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicsTierName) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTopicsTierName:
    return cast(GuardrailTopicsTierName, data)
