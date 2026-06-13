"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOwnership``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailOwnership: TypeAlias = Literal[
    "SELF",
    "CROSS_ACCOUNT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELF",
        "CROSS_ACCOUNT",
    )
)


def serialize_json(value: GuardrailOwnership) -> str:
    return value


def deserialize_json(data: str) -> GuardrailOwnership:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailOwnership value: {data!r}")
    return cast(GuardrailOwnership, data)
