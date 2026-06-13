"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseImageFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailConverseImageFormat: TypeAlias = Literal[
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


def serialize_json(value: GuardrailConverseImageFormat) -> str:
    return value


def deserialize_json(data: str) -> GuardrailConverseImageFormat:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailConverseImageFormat value: {data!r}"
        )
    return cast(GuardrailConverseImageFormat, data)
