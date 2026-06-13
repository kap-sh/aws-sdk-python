"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicRefreshStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TopicRefreshStatus: TypeAlias = Literal[
    "INITIALIZED",
    "RUNNING",
    "FAILED",
    "COMPLETED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZED",
        "RUNNING",
        "FAILED",
        "COMPLETED",
        "CANCELLED",
    )
)


def serialize_json(value: TopicRefreshStatus) -> str:
    return value


def deserialize_json(data: str) -> TopicRefreshStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopicRefreshStatus value: {data!r}")
    return cast(TopicRefreshStatus, data)
