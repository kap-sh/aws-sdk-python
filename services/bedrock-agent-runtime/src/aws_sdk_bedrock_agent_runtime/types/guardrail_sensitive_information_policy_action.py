"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailSensitiveInformationPolicyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

GuardrailSensitiveInformationPolicyAction: TypeAlias = Literal[
    "BLOCKED",
    "ANONYMIZED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLOCKED",
        "ANONYMIZED",
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
