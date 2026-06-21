"""Generated from Smithy shape ``com.amazonaws.deadline#StepTargetTaskRunStatus``."""

from typing import Literal, TypeAlias, cast

StepTargetTaskRunStatus: TypeAlias = Literal[
    "READY",
    "FAILED",
    "SUCCEEDED",
    "CANCELED",
    "SUSPENDED",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: StepTargetTaskRunStatus) -> str:
    return value


def deserialize_json(data: str) -> StepTargetTaskRunStatus:
    return cast(StepTargetTaskRunStatus, data)
