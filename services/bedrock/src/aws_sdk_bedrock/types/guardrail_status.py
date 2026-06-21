"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailStatus``."""

from typing import Literal, TypeAlias, cast

GuardrailStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "VERSIONING",
    "READY",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailStatus) -> str:
    return value


def deserialize_json(data: str) -> GuardrailStatus:
    return cast(GuardrailStatus, data)
