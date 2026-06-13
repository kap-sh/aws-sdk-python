"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailSensitiveInformationPolicyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailSensitiveInformationPolicyAction: TypeAlias = Literal[
    "ANONYMIZED",
    "BLOCKED",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ANONYMIZED",
        "BLOCKED",
        "NONE",
    )
)


def serialize_json(value: GuardrailSensitiveInformationPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailSensitiveInformationPolicyAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailSensitiveInformationPolicyAction value: {data!r}"
        )
    return cast(GuardrailSensitiveInformationPolicyAction, data)
