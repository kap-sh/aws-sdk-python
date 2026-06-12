"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobExecutionFailureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

IoTJobExecutionFailureType: TypeAlias = Literal[
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


def serialize_json(value: IoTJobExecutionFailureType) -> str:
    return value


def deserialize_json(data: str) -> IoTJobExecutionFailureType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IoTJobExecutionFailureType value: {data!r}"
        )
    return cast(IoTJobExecutionFailureType, data)
