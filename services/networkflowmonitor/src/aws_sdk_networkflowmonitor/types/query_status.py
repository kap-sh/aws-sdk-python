"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#QueryStatus``."""

from typing import Literal, TypeAlias, cast

QueryStatus: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "CANCELED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryStatus) -> str:
    return value


def deserialize_json(data: str) -> QueryStatus:
    return cast(QueryStatus, data)
