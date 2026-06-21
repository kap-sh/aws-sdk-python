"""Generated from Smithy shape ``com.amazonaws.appsync#FieldLogLevel``."""

from typing import Literal, TypeAlias, cast

FieldLogLevel: TypeAlias = Literal[
    "NONE",
    "ERROR",
    "ALL",
    "INFO",
    "DEBUG",
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldLogLevel) -> str:
    return value


def deserialize_json(data: str) -> FieldLogLevel:
    return cast(FieldLogLevel, data)
