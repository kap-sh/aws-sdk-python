"""Generated from Smithy shape ``com.amazonaws.greengrass#LoggerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

LoggerType: TypeAlias = Literal[
    "FileSystem",
    "AWSCloudWatch",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FileSystem",
        "AWSCloudWatch",
    )
)


def serialize_json(value: LoggerType) -> str:
    return value


def deserialize_json(data: str) -> LoggerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoggerType value: {data!r}")
    return cast(LoggerType, data)
