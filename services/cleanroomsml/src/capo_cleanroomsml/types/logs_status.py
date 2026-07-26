"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#LogsStatus``."""

from typing import Literal, TypeAlias, cast

LogsStatus: TypeAlias = Literal[
    "PUBLISH_SUCCEEDED",
    "PUBLISH_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogsStatus) -> str:
    return value


def deserialize_json(data: str) -> LogsStatus:
    return cast(LogsStatus, data)
