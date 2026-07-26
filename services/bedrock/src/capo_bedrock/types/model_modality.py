"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelModality``."""

from typing import Literal, TypeAlias, cast

ModelModality: TypeAlias = Literal[
    "TEXT",
    "IMAGE",
    "EMBEDDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelModality) -> str:
    return value


def deserialize_json(data: str) -> ModelModality:
    return cast(ModelModality, data)
