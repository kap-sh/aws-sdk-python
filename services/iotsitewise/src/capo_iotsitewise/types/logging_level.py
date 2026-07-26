"""Generated from Smithy shape ``com.amazonaws.iotsitewise#LoggingLevel``."""

from typing import Literal, TypeAlias, cast

LoggingLevel: TypeAlias = Literal[
    "ERROR",
    "INFO",
    "OFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: LoggingLevel) -> str:
    return value


def deserialize_json(data: str) -> LoggingLevel:
    return cast(LoggingLevel, data)
