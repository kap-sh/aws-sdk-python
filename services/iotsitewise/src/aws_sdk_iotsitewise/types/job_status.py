"""Generated from Smithy shape ``com.amazonaws.iotsitewise#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "PENDING",
    "CANCELLED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "COMPLETED_WITH_FAILURES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "CANCELLED",
        "RUNNING",
        "COMPLETED",
        "FAILED",
        "COMPLETED_WITH_FAILURES",
    )
)


def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
