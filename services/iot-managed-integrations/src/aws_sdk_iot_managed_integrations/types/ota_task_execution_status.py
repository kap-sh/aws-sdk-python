"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskExecutionStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: OtaTaskExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> OtaTaskExecutionStatus:
    return cast(OtaTaskExecutionStatus, data)
