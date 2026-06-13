"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailStreamProcessingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailStreamProcessingMode: TypeAlias = Literal[
    "sync",
    "async",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "sync",
        "async",
    )
)


def serialize_json(value: GuardrailStreamProcessingMode) -> str:
    return value


def deserialize_json(data: str) -> GuardrailStreamProcessingMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailStreamProcessingMode value: {data!r}"
        )
    return cast(GuardrailStreamProcessingMode, data)
