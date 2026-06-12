"""Generated from Smithy shape ``com.amazonaws.mediatailor#LoggingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

LoggingStrategy: TypeAlias = Literal[
    "VENDED_LOGS",
    "LEGACY_CLOUDWATCH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VENDED_LOGS",
        "LEGACY_CLOUDWATCH",
    )
)


def serialize_json(value: LoggingStrategy) -> str:
    return value


def deserialize_json(data: str) -> LoggingStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoggingStrategy value: {data!r}")
    return cast(LoggingStrategy, data)
