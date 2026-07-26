"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCustomizationJobStatus``."""

from typing import Literal, TypeAlias, cast

ModelCustomizationJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelCustomizationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelCustomizationJobStatus:
    return cast(ModelCustomizationJobStatus, data)
