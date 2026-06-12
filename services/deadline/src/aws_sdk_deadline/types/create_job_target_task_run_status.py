"""Generated from Smithy shape ``com.amazonaws.deadline#CreateJobTargetTaskRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

CreateJobTargetTaskRunStatus: TypeAlias = Literal[
    "READY",
    "SUSPENDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "SUSPENDED",
    )
)


def serialize_json(value: CreateJobTargetTaskRunStatus) -> str:
    return value


def deserialize_json(data: str) -> CreateJobTargetTaskRunStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CreateJobTargetTaskRunStatus value: {data!r}"
        )
    return cast(CreateJobTargetTaskRunStatus, data)
