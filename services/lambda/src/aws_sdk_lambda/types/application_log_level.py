"""Generated from Smithy shape ``com.amazonaws.lambda#ApplicationLogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

ApplicationLogLevel: TypeAlias = Literal[
    "TRACE",
    "DEBUG",
    "INFO",
    "WARN",
    "ERROR",
    "FATAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRACE",
        "DEBUG",
        "INFO",
        "WARN",
        "ERROR",
        "FATAL",
    )
)


def serialize_json(value: ApplicationLogLevel) -> str:
    return value


def deserialize_json(data: str) -> ApplicationLogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationLogLevel value: {data!r}")
    return cast(ApplicationLogLevel, data)
