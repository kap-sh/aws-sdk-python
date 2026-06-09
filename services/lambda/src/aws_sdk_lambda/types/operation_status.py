"""Generated from Smithy shape ``com.amazonaws.lambda#OperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

OperationStatus: TypeAlias = Literal[
    "STARTED",
    "PENDING",
    "READY",
    "SUCCEEDED",
    "FAILED",
    "CANCELLED",
    "TIMED_OUT",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTED",
        "PENDING",
        "READY",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "TIMED_OUT",
        "STOPPED",
    )
)


def serialize_json(value: OperationStatus) -> str:
    return value


def deserialize_json(data: str) -> OperationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationStatus value: {data!r}")
    return cast(OperationStatus, data)
