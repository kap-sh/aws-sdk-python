"""Generated from Smithy shape ``com.amazonaws.appsync#FieldLogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

FieldLogLevel: TypeAlias = Literal[
    "NONE",
    "ERROR",
    "ALL",
    "INFO",
    "DEBUG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "ERROR",
        "ALL",
        "INFO",
        "DEBUG",
    )
)


def serialize_json(value: FieldLogLevel) -> str:
    return value


def deserialize_json(data: str) -> FieldLogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FieldLogLevel value: {data!r}")
    return cast(FieldLogLevel, data)
