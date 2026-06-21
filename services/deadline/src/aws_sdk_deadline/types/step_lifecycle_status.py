"""Generated from Smithy shape ``com.amazonaws.deadline#StepLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

StepLifecycleStatus: TypeAlias = Literal[
    "CREATE_COMPLETE",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_SUCCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: StepLifecycleStatus) -> str:
    return value


def deserialize_json(data: str) -> StepLifecycleStatus:
    return cast(StepLifecycleStatus, data)
