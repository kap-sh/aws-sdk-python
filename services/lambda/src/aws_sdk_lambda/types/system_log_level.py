"""Generated from Smithy shape ``com.amazonaws.lambda#SystemLogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

SystemLogLevel: TypeAlias = Literal[
    "DEBUG",
    "INFO",
    "WARN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEBUG",
        "INFO",
        "WARN",
    )
)


def serialize_json(value: SystemLogLevel) -> str:
    return value


def deserialize_json(data: str) -> SystemLogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SystemLogLevel value: {data!r}")
    return cast(SystemLogLevel, data)
