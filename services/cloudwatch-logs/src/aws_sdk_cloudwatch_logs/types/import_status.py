"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ImportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

ImportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELLED",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "CANCELLED",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: ImportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportStatus value: {data!r}")
    return cast(ImportStatus, data)
