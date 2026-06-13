"""Generated from Smithy shape ``com.amazonaws.connecthealth#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
    )
)


def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
