"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailContentFilterConfidence``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

GuardrailContentFilterConfidence: TypeAlias = Literal[
    "NONE",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_json(value: GuardrailContentFilterConfidence) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentFilterConfidence:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailContentFilterConfidence value: {data!r}"
        )
    return cast(GuardrailContentFilterConfidence, data)
