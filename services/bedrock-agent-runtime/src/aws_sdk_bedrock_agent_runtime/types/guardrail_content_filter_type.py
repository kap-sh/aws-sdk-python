"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailContentFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

GuardrailContentFilterType: TypeAlias = Literal[
    "INSULTS",
    "HATE",
    "SEXUAL",
    "VIOLENCE",
    "MISCONDUCT",
    "PROMPT_ATTACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSULTS",
        "HATE",
        "SEXUAL",
        "VIOLENCE",
        "MISCONDUCT",
        "PROMPT_ATTACK",
    )
)


def serialize_json(value: GuardrailContentFilterType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentFilterType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailContentFilterType value: {data!r}"
        )
    return cast(GuardrailContentFilterType, data)
