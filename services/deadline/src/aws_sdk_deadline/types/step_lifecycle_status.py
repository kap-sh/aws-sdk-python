"""Generated from Smithy shape ``com.amazonaws.deadline#StepLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

StepLifecycleStatus: TypeAlias = Literal[
    "CREATE_COMPLETE",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_SUCCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_COMPLETE",
        "UPDATE_IN_PROGRESS",
        "UPDATE_FAILED",
        "UPDATE_SUCCEEDED",
    )
)


def serialize_json(value: StepLifecycleStatus) -> str:
    return value


def deserialize_json(data: str) -> StepLifecycleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepLifecycleStatus value: {data!r}")
    return cast(StepLifecycleStatus, data)
