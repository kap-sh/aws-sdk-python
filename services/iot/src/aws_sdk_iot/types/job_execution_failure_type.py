"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionFailureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

JobExecutionFailureType: TypeAlias = Literal[
    "FAILED",
    "REJECTED",
    "TIMED_OUT",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "REJECTED",
        "TIMED_OUT",
        "ALL",
    )
)


def serialize_json(value: JobExecutionFailureType) -> str:
    return value


def deserialize_json(data: str) -> JobExecutionFailureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobExecutionFailureType value: {data!r}")
    return cast(JobExecutionFailureType, data)
