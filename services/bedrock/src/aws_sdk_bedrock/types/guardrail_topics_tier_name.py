"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicsTierName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailTopicsTierName: TypeAlias = Literal[
    "CLASSIC",
    "STANDARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLASSIC",
        "STANDARD",
    )
)


def serialize_json(value: GuardrailTopicsTierName) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTopicsTierName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailTopicsTierName value: {data!r}")
    return cast(GuardrailTopicsTierName, data)
