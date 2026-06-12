"""Generated from Smithy shape ``com.amazonaws.datasync#LogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

LogLevel: TypeAlias = Literal[
    "OFF",
    "BASIC",
    "TRANSFER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "BASIC",
        "TRANSFER",
    )
)


def serialize_aws_json_1_1(value: LogLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogLevel value: {data!r}")
    return cast(LogLevel, data)
