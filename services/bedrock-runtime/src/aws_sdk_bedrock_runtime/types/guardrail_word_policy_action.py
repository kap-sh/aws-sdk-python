"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailWordPolicyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailWordPolicyAction: TypeAlias = Literal[
    "BLOCKED",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLOCKED",
        "NONE",
    )
)


def serialize_json(value: GuardrailWordPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailWordPolicyAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailWordPolicyAction value: {data!r}")
    return cast(GuardrailWordPolicyAction, data)
