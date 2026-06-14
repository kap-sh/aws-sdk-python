"""Generated from Smithy shape ``com.amazonaws.datazone#JobRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

JobRunStatus: TypeAlias = Literal[
    "SCHEDULED",
    "IN_PROGRESS",
    "SUCCESS",
    "PARTIALLY_SUCCEEDED",
    "FAILED",
    "ABORTED",
    "TIMED_OUT",
    "CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "IN_PROGRESS",
        "SUCCESS",
        "PARTIALLY_SUCCEEDED",
        "FAILED",
        "ABORTED",
        "TIMED_OUT",
        "CANCELED",
    )
)


def serialize_json(value: JobRunStatus) -> str:
    return value


def deserialize_json(data: str) -> JobRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobRunStatus value: {data!r}")
    return cast(JobRunStatus, data)
