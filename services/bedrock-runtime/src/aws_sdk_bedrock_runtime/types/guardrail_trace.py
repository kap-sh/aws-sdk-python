"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTrace``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailTrace: TypeAlias = Literal[
    "enabled",
    "disabled",
    "enabled_full",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
        "enabled_full",
    )
)


def serialize_json(value: GuardrailTrace) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTrace:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailTrace value: {data!r}")
    return cast(GuardrailTrace, data)
