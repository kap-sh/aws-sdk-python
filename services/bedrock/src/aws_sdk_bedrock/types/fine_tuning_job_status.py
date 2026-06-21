"""Generated from Smithy shape ``com.amazonaws.bedrock#FineTuningJobStatus``."""

from typing import Literal, TypeAlias, cast

FineTuningJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- restJson1 ser/de ---
def serialize_json(value: FineTuningJobStatus) -> str:
    return value


def deserialize_json(data: str) -> FineTuningJobStatus:
    return cast(FineTuningJobStatus, data)
