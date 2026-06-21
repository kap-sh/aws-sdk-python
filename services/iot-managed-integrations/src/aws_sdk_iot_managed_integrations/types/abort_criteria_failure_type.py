"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AbortCriteriaFailureType``."""

from typing import Literal, TypeAlias, cast

AbortCriteriaFailureType: TypeAlias = Literal[
    "FAILED",
    "REJECTED",
    "TIMED_OUT",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AbortCriteriaFailureType) -> str:
    return value


def deserialize_json(data: str) -> AbortCriteriaFailureType:
    return cast(AbortCriteriaFailureType, data)
