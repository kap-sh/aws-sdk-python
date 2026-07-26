"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionResourceStatus``."""

from typing import Literal, TypeAlias, cast

LifecycleExecutionResourceStatus: TypeAlias = Literal[
    "FAILED",
    "IN_PROGRESS",
    "SKIPPED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> LifecycleExecutionResourceStatus:
    return cast(LifecycleExecutionResourceStatus, data)
