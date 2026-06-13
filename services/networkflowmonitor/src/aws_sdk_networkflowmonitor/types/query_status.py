"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#QueryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkflowmonitor.errors import DeserializationError

QueryStatus: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELED",
    )
)


def serialize_json(value: QueryStatus) -> str:
    return value


def deserialize_json(data: str) -> QueryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryStatus value: {data!r}")
    return cast(QueryStatus, data)
