"""Generated from Smithy shape ``com.amazonaws.cognitosync#StreamingStatus``."""

from typing import Literal, TypeAlias, cast

StreamingStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamingStatus) -> str:
    return value


def deserialize_json(data: str) -> StreamingStatus:
    return cast(StreamingStatus, data)
