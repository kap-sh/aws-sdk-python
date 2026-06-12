"""Generated from Smithy shape ``com.amazonaws.codebuild#StatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

StatusType: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "FAULT",
    "TIMED_OUT",
    "IN_PROGRESS",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
        "FAULT",
        "TIMED_OUT",
        "IN_PROGRESS",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: StatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusType value: {data!r}")
    return cast(StatusType, data)
