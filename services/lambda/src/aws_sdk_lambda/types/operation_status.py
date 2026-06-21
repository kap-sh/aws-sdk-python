"""Generated from Smithy shape ``com.amazonaws.lambda#OperationStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: OperationStatus) -> str:
    return value


def deserialize_json(data: str) -> OperationStatus:
    return cast(OperationStatus, data)
