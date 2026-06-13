"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailWordAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailWordAction: TypeAlias = Literal[
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


def serialize_json(value: GuardrailWordAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailWordAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailWordAction value: {data!r}")
    return cast(GuardrailWordAction, data)
