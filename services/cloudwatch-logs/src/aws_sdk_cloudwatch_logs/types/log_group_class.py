"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

LogGroupClass: TypeAlias = Literal[
    "STANDARD",
    "INFREQUENT_ACCESS",
    "DELIVERY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "INFREQUENT_ACCESS",
        "DELIVERY",
    )
)


def serialize_aws_json_1_1(value: LogGroupClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogGroupClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogGroupClass value: {data!r}")
    return cast(LogGroupClass, data)
