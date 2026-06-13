"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailAction: TypeAlias = Literal[
    "NONE",
    "GUARDRAIL_INTERVENED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "GUARDRAIL_INTERVENED",
    )
)


def serialize_json(value: GuardrailAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailAction value: {data!r}")
    return cast(GuardrailAction, data)
