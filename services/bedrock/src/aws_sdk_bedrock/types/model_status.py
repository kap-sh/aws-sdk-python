"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelStatus``."""

from typing import Literal, TypeAlias, cast

ModelStatus: TypeAlias = Literal[
    "Active",
    "Creating",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelStatus:
    return cast(ModelStatus, data)
