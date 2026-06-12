"""Generated from Smithy shape ``com.amazonaws.amplify#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "CREATED",
    "PENDING",
    "PROVISIONING",
    "RUNNING",
    "FAILED",
    "SUCCEED",
    "CANCELLING",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "PENDING",
        "PROVISIONING",
        "RUNNING",
        "FAILED",
        "SUCCEED",
        "CANCELLING",
        "CANCELLED",
    )
)


def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
