"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailSensitiveInformationPolicyAction``."""

from typing import Literal, TypeAlias, cast

GuardrailSensitiveInformationPolicyAction: TypeAlias = Literal[
    "ANONYMIZED",
    "BLOCKED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSensitiveInformationPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailSensitiveInformationPolicyAction:
    return cast(GuardrailSensitiveInformationPolicyAction, data)
