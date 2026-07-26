"""Generated from Smithy shape ``com.amazonaws.iot#RetryableFailureType``."""

from typing import Literal, TypeAlias, cast

RetryableFailureType: TypeAlias = Literal[
    "FAILED",
    "TIMED_OUT",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetryableFailureType) -> str:
    return value


def deserialize_json(data: str) -> RetryableFailureType:
    return cast(RetryableFailureType, data)
