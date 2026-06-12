"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

OtaTaskExecutionStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
    "REJECTED",
    "REMOVED",
    "CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "TIMED_OUT",
        "REJECTED",
        "REMOVED",
        "CANCELED",
    )
)


def serialize_json(value: OtaTaskExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> OtaTaskExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OtaTaskExecutionStatus value: {data!r}")
    return cast(OtaTaskExecutionStatus, data)
