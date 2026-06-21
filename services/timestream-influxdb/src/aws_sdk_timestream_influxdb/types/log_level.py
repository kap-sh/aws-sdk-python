"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#LogLevel``."""

from typing import Literal, TypeAlias, cast

LogLevel: TypeAlias = Literal[
    "debug",
    "info",
    "error",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LogLevel:
    return cast(LogLevel, data)
