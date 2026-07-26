"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobStatus``."""

from typing import Literal, TypeAlias, cast

ModelInvocationJobStatus: TypeAlias = Literal[
    "Submitted",
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
    "PartiallyCompleted",
    "Expired",
    "Validating",
    "Scheduled",
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelInvocationJobStatus:
    return cast(ModelInvocationJobStatus, data)
