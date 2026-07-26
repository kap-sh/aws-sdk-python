"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelImportJobStatus``."""

from typing import Literal, TypeAlias, cast

ModelImportJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelImportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelImportJobStatus:
    return cast(ModelImportJobStatus, data)
