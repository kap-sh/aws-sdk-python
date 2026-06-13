"""Generated from Smithy shape ``com.amazonaws.backupsearch#SearchJobState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backupsearch.errors import DeserializationError

SearchJobState: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "STOPPING",
    "STOPPED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "COMPLETED",
        "STOPPING",
        "STOPPED",
        "FAILED",
    )
)


def serialize_json(value: SearchJobState) -> str:
    return value


def deserialize_json(data: str) -> SearchJobState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchJobState value: {data!r}")
    return cast(SearchJobState, data)
