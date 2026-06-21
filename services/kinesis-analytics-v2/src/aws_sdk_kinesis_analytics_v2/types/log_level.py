"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#LogLevel``."""

from typing import Literal, TypeAlias, cast

LogLevel: TypeAlias = Literal[
    "INFO",
    "WARN",
    "ERROR",
    "DEBUG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogLevel:
    return cast(LogLevel, data)
