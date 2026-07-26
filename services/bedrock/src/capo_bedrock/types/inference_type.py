"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceType``."""

from typing import Literal, TypeAlias, cast

InferenceType: TypeAlias = Literal[
    "ON_DEMAND",
    "PROVISIONED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InferenceType) -> str:
    return value


def deserialize_json(data: str) -> InferenceType:
    return cast(InferenceType, data)
