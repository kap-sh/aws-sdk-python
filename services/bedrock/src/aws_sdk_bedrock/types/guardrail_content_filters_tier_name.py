"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentFiltersTierName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailContentFiltersTierName: TypeAlias = Literal[
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


def serialize_json(value: GuardrailContentFiltersTierName) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentFiltersTierName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailContentFiltersTierName value: {data!r}"
        )
    return cast(GuardrailContentFiltersTierName, data)
