"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#LogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

LogLevel: TypeAlias = Literal[
    "INFO",
    "WARN",
    "ERROR",
    "DEBUG",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFO",
        "WARN",
        "ERROR",
        "DEBUG",
    )
)


def serialize_aws_json_1_1(value: LogLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogLevel value: {data!r}")
    return cast(LogLevel, data)
