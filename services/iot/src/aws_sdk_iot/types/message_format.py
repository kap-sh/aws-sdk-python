"""Generated from Smithy shape ``com.amazonaws.iot#MessageFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

MessageFormat: TypeAlias = Literal[
    "RAW",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RAW",
        "JSON",
    )
)


def serialize_json(value: MessageFormat) -> str:
    return value


def deserialize_json(data: str) -> MessageFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageFormat value: {data!r}")
    return cast(MessageFormat, data)
