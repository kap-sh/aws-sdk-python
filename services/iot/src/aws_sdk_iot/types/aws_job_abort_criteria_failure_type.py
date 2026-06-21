"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobAbortCriteriaFailureType``."""

from typing import Literal, TypeAlias, cast

AwsJobAbortCriteriaFailureType: TypeAlias = Literal[
    "FAILED",
    "REJECTED",
    "TIMED_OUT",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobAbortCriteriaFailureType) -> str:
    return value


def deserialize_json(data: str) -> AwsJobAbortCriteriaFailureType:
    return cast(AwsJobAbortCriteriaFailureType, data)
