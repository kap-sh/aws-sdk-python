"""Generated from Smithy shape ``com.amazonaws.lambda#LogType``."""

from typing import Literal, TypeAlias, cast

LogType: TypeAlias = Literal[
    "None",
    "Tail",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    return cast(LogType, data)
