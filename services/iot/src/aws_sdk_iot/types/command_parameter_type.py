"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

CommandParameterType: TypeAlias = Literal[
    "STRING",
    "INTEGER",
    "DOUBLE",
    "LONG",
    "UNSIGNEDLONG",
    "BOOLEAN",
    "BINARY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "INTEGER",
        "DOUBLE",
        "LONG",
        "UNSIGNEDLONG",
        "BOOLEAN",
        "BINARY",
    )
)


def serialize_json(value: CommandParameterType) -> str:
    return value


def deserialize_json(data: str) -> CommandParameterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommandParameterType value: {data!r}")
    return cast(CommandParameterType, data)
