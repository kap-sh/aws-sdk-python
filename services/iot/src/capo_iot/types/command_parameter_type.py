"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: CommandParameterType) -> str:
    return value


def deserialize_json(data: str) -> CommandParameterType:
    return cast(CommandParameterType, data)
