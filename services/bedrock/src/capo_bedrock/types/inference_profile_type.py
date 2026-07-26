"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceProfileType``."""

from typing import Literal, TypeAlias, cast

InferenceProfileType: TypeAlias = Literal[
    "SYSTEM_DEFINED",
    "APPLICATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: InferenceProfileType) -> str:
    return value


def deserialize_json(data: str) -> InferenceProfileType:
    return cast(InferenceProfileType, data)
