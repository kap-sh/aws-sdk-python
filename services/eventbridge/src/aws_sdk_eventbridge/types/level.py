"""Generated from Smithy shape ``com.amazonaws.eventbridge#Level``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

Level: TypeAlias = Literal[
    "OFF",
    "ERROR",
    "INFO",
    "TRACE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "ERROR",
        "INFO",
        "TRACE",
    )
)


def serialize_aws_json_1_1(value: Level) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Level:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Level value: {data!r}")
    return cast(Level, data)
