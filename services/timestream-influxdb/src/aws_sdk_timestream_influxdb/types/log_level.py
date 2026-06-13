"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#LogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_influxdb.errors import DeserializationError

LogLevel: TypeAlias = Literal[
    "debug",
    "info",
    "error",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "debug",
        "info",
        "error",
    )
)


def serialize_aws_json_1_0(value: LogLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogLevel value: {data!r}")
    return cast(LogLevel, data)
