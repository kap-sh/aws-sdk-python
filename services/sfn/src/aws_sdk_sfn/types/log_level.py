"""Generated from Smithy shape ``com.amazonaws.sfn#LogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

LogLevel: TypeAlias = Literal[
    "ALL",
    "ERROR",
    "FATAL",
    "OFF",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ERROR",
        "FATAL",
        "OFF",
    )
)


def serialize_aws_json_1_0(value: LogLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogLevel value: {data!r}")
    return cast(LogLevel, data)
