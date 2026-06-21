"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicRefreshStatus``."""

from typing import Literal, TypeAlias, cast

TopicRefreshStatus: TypeAlias = Literal[
    "INITIALIZED",
    "RUNNING",
    "FAILED",
    "COMPLETED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicRefreshStatus) -> str:
    return value


def deserialize_json(data: str) -> TopicRefreshStatus:
    return cast(TopicRefreshStatus, data)
