"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContextualGroundingPolicyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailContextualGroundingPolicyAction: TypeAlias = Literal[
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


def serialize_json(value: GuardrailContextualGroundingPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContextualGroundingPolicyAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailContextualGroundingPolicyAction value: {data!r}"
        )
    return cast(GuardrailContextualGroundingPolicyAction, data)
