"""Generated from Smithy shape ``com.amazonaws.cloudtrail#QueryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

QueryStatus: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "FINISHED",
    "FAILED",
    "CANCELLED",
    "TIMED_OUT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "RUNNING",
        "FINISHED",
        "FAILED",
        "CANCELLED",
        "TIMED_OUT",
    )
)


def serialize_aws_json_1_1(value: QueryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryStatus value: {data!r}")
    return cast(QueryStatus, data)
