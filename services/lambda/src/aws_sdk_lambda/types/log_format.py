"""Generated from Smithy shape ``com.amazonaws.lambda#LogFormat``."""

from typing import Literal, TypeAlias, cast

LogFormat: TypeAlias = Literal[
    "JSON",
    "Text",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogFormat) -> str:
    return value


def deserialize_json(data: str) -> LogFormat:
    return cast(LogFormat, data)
