"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#RetryCriteriaFailureType``."""

from typing import Literal, TypeAlias, cast

RetryCriteriaFailureType: TypeAlias = Literal[
    "FAILED",
    "TIMED_OUT",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetryCriteriaFailureType) -> str:
    return value


def deserialize_json(data: str) -> RetryCriteriaFailureType:
    return cast(RetryCriteriaFailureType, data)
