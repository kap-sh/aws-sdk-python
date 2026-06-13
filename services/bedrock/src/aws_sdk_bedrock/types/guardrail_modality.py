"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailModality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailModality: TypeAlias = Literal[
    "TEXT",
    "IMAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT",
        "IMAGE",
    )
)


def serialize_json(value: GuardrailModality) -> str:
    return value


def deserialize_json(data: str) -> GuardrailModality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailModality value: {data!r}")
    return cast(GuardrailModality, data)
