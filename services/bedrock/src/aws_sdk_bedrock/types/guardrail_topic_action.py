"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailTopicAction: TypeAlias = Literal[
    "BLOCK",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLOCK",
        "NONE",
    )
)


def serialize_json(value: GuardrailTopicAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTopicAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailTopicAction value: {data!r}")
    return cast(GuardrailTopicAction, data)
