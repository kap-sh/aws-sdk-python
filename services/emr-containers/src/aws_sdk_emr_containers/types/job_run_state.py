"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobRunState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr_containers.errors import DeserializationError

JobRunState: TypeAlias = Literal[
    "PENDING",
    "SUBMITTED",
    "RUNNING",
    "FAILED",
    "CANCELLED",
    "CANCEL_PENDING",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SUBMITTED",
        "RUNNING",
        "FAILED",
        "CANCELLED",
        "CANCEL_PENDING",
        "COMPLETED",
    )
)


def serialize_json(value: JobRunState) -> str:
    return value


def deserialize_json(data: str) -> JobRunState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobRunState value: {data!r}")
    return cast(JobRunState, data)
