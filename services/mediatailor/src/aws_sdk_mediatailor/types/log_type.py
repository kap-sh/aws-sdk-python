"""Generated from Smithy shape ``com.amazonaws.mediatailor#LogType``."""

from typing import Literal, TypeAlias, cast

LogType: TypeAlias = Literal["AS_RUN",]


# --- restJson1 ser/de ---
def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    return cast(LogType, data)
