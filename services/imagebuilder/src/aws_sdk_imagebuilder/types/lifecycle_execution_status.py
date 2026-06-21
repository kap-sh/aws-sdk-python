"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionStatus``."""

from typing import Literal, TypeAlias, cast

LifecycleExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELLED",
    "CANCELLING",
    "FAILED",
    "SUCCESS",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> LifecycleExecutionStatus:
    return cast(LifecycleExecutionStatus, data)
