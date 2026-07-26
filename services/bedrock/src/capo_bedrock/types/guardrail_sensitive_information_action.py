"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailSensitiveInformationAction``."""

from typing import Literal, TypeAlias, cast

GuardrailSensitiveInformationAction: TypeAlias = Literal[
    "BLOCK",
    "ANONYMIZE",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSensitiveInformationAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailSensitiveInformationAction:
    return cast(GuardrailSensitiveInformationAction, data)
