"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCopyJobStatus``."""

from typing import Literal, TypeAlias, cast

ModelCopyJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelCopyJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelCopyJobStatus:
    return cast(ModelCopyJobStatus, data)
