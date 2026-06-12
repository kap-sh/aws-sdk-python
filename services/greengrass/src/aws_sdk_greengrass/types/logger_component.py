"""Generated from Smithy shape ``com.amazonaws.greengrass#LoggerComponent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

LoggerComponent: TypeAlias = Literal[
    "GreengrassSystem",
    "Lambda",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GreengrassSystem",
        "Lambda",
    )
)


def serialize_json(value: LoggerComponent) -> str:
    return value


def deserialize_json(data: str) -> LoggerComponent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoggerComponent value: {data!r}")
    return cast(LoggerComponent, data)
