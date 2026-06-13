"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailContentFilterType: TypeAlias = Literal[
    "SEXUAL",
    "VIOLENCE",
    "HATE",
    "INSULTS",
    "MISCONDUCT",
    "PROMPT_ATTACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEXUAL",
        "VIOLENCE",
        "HATE",
        "INSULTS",
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
