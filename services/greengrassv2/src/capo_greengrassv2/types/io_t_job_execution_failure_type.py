"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobExecutionFailureType``."""

from typing import Literal, TypeAlias, cast

IoTJobExecutionFailureType: TypeAlias = Literal[
    "FAILED",
    "REJECTED",
    "TIMED_OUT",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: IoTJobExecutionFailureType) -> str:
    return value


def deserialize_json(data: str) -> IoTJobExecutionFailureType:
    return cast(IoTJobExecutionFailureType, data)
