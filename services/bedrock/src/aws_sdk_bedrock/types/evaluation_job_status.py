"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationJobStatus``."""

from typing import Literal, TypeAlias, cast

EvaluationJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
    "Deleting",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationJobStatus:
    return cast(EvaluationJobStatus, data)
