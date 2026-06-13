"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentPolicyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailContentPolicyAction: TypeAlias = Literal[
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


def serialize_json(value: GuardrailContentPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentPolicyAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailContentPolicyAction value: {data!r}"
        )
    return cast(GuardrailContentPolicyAction, data)
