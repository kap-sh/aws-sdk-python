"""Generated from Smithy shape ``com.amazonaws.backupsearch#SearchJobState``."""

from typing import Literal, TypeAlias, cast

SearchJobState: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "STOPPING",
    "STOPPED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobState) -> str:
    return value


def deserialize_json(data: str) -> SearchJobState:
    return cast(SearchJobState, data)
