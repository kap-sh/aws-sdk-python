"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#JobExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_jobs_data_plane.errors import DeserializationError

JobExecutionStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
    "REJECTED",
    "REMOVED",
    "CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "TIMED_OUT",
        "REJECTED",
        "REMOVED",
        "CANCELED",
    )
)


def serialize_json(value: JobExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> JobExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobExecutionStatus value: {data!r}")
    return cast(JobExecutionStatus, data)
