"""Generated from Smithy shape ``com.amazonaws.iotsitewise#LoggingLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

LoggingLevel: TypeAlias = Literal[
    "ERROR",
    "INFO",
    "OFF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ERROR",
        "INFO",
        "OFF",
    )
)


def serialize_json(value: LoggingLevel) -> str:
    return value


def deserialize_json(data: str) -> LoggingLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoggingLevel value: {data!r}")
    return cast(LoggingLevel, data)
