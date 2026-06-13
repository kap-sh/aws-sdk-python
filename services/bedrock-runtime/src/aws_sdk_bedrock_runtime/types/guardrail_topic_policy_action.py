"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTopicPolicyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailTopicPolicyAction: TypeAlias = Literal[
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


def serialize_json(value: GuardrailTopicPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTopicPolicyAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailTopicPolicyAction value: {data!r}"
        )
    return cast(GuardrailTopicPolicyAction, data)
