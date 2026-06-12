"""Generated from Smithy shape ``com.amazonaws.deadline#StepTargetTaskRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

StepTargetTaskRunStatus: TypeAlias = Literal[
    "READY",
    "FAILED",
    "SUCCEEDED",
    "CANCELED",
    "SUSPENDED",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "FAILED",
        "SUCCEEDED",
        "CANCELED",
        "SUSPENDED",
        "PENDING",
    )
)


def serialize_json(value: StepTargetTaskRunStatus) -> str:
    return value


def deserialize_json(data: str) -> StepTargetTaskRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepTargetTaskRunStatus value: {data!r}")
    return cast(StepTargetTaskRunStatus, data)
