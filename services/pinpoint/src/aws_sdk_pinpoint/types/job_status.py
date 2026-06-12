"""Generated from Smithy shape ``com.amazonaws.pinpoint#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "CREATED",
    "PREPARING_FOR_INITIALIZATION",
    "INITIALIZING",
    "PROCESSING",
    "PENDING_JOB",
    "COMPLETING",
    "COMPLETED",
    "FAILING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "PREPARING_FOR_INITIALIZATION",
        "INITIALIZING",
        "PROCESSING",
        "PENDING_JOB",
        "COMPLETING",
        "COMPLETED",
        "FAILING",
        "FAILED",
    )
)


def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
