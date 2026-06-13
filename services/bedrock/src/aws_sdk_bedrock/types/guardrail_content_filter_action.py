"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentFilterAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailContentFilterAction: TypeAlias = Literal[
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


def serialize_json(value: GuardrailContentFilterAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentFilterAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailContentFilterAction value: {data!r}"
        )
    return cast(GuardrailContentFilterAction, data)
