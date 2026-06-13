"""Generated from Smithy shape ``com.amazonaws.entityresolution#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "QUEUED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "QUEUED",
    )
)


def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
