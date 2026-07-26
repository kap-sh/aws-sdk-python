"""Generated from Smithy shape ``com.amazonaws.sfn#LogLevel``."""

from typing import Literal, TypeAlias, cast

LogLevel: TypeAlias = Literal[
    "ALL",
    "ERROR",
    "FATAL",
    "OFF",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LogLevel:
    return cast(LogLevel, data)
