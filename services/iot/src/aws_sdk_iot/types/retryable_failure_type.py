"""Generated from Smithy shape ``com.amazonaws.iot#RetryableFailureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

RetryableFailureType: TypeAlias = Literal[
    "FAILED",
    "TIMED_OUT",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "TIMED_OUT",
        "ALL",
    )
)


def serialize_json(value: RetryableFailureType) -> str:
    return value


def deserialize_json(data: str) -> RetryableFailureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetryableFailureType value: {data!r}")
    return cast(RetryableFailureType, data)
