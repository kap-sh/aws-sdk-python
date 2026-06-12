"""Generated from Smithy shape ``com.amazonaws.iot#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELED",
    "COMPLETED",
    "DELETION_IN_PROGRESS",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "CANCELED",
        "COMPLETED",
        "DELETION_IN_PROGRESS",
        "SCHEDULED",
    )
)


def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
