"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#LogType``."""

from typing import Literal, TypeAlias, cast

LogType: TypeAlias = Literal[
    "ALL",
    "ERROR_SUMMARY",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    return cast(LogType, data)
