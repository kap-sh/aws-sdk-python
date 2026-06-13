"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailImageFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailImageFormat: TypeAlias = Literal[
    "png",
    "jpeg",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "png",
        "jpeg",
    )
)


def serialize_json(value: GuardrailImageFormat) -> str:
    return value


def deserialize_json(data: str) -> GuardrailImageFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailImageFormat value: {data!r}")
    return cast(GuardrailImageFormat, data)
