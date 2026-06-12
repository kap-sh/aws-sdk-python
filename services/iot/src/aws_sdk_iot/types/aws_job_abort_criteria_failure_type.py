"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobAbortCriteriaFailureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AwsJobAbortCriteriaFailureType: TypeAlias = Literal[
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


def serialize_json(value: AwsJobAbortCriteriaFailureType) -> str:
    return value


def deserialize_json(data: str) -> AwsJobAbortCriteriaFailureType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AwsJobAbortCriteriaFailureType value: {data!r}"
        )
    return cast(AwsJobAbortCriteriaFailureType, data)
