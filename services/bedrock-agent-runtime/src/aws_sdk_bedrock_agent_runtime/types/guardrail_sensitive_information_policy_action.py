"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailSensitiveInformationPolicyAction``."""

from typing import Literal, TypeAlias, cast

GuardrailSensitiveInformationPolicyAction: TypeAlias = Literal[
    "BLOCKED",
    "ANONYMIZED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSensitiveInformationPolicyAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailSensitiveInformationPolicyAction:
    return cast(GuardrailSensitiveInformationPolicyAction, data)
