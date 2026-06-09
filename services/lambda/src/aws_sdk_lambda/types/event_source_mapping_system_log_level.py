"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourceMappingSystemLogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

EventSourceMappingSystemLogLevel: TypeAlias = Literal[
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


def serialize_json(value: EventSourceMappingSystemLogLevel) -> str:
    return value


def deserialize_json(data: str) -> EventSourceMappingSystemLogLevel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EventSourceMappingSystemLogLevel value: {data!r}"
        )
    return cast(EventSourceMappingSystemLogLevel, data)
