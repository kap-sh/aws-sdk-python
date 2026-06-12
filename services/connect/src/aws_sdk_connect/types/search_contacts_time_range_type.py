"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsTimeRangeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

SearchContactsTimeRangeType: TypeAlias = Literal[
    "INITIATION_TIMESTAMP",
    "SCHEDULED_TIMESTAMP",
    "CONNECTED_TO_AGENT_TIMESTAMP",
    "DISCONNECT_TIMESTAMP",
    "ENQUEUE_TIMESTAMP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIATION_TIMESTAMP",
        "SCHEDULED_TIMESTAMP",
        "CONNECTED_TO_AGENT_TIMESTAMP",
        "DISCONNECT_TIMESTAMP",
        "ENQUEUE_TIMESTAMP",
    )
)


def serialize_json(value: SearchContactsTimeRangeType) -> str:
    return value


def deserialize_json(data: str) -> SearchContactsTimeRangeType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SearchContactsTimeRangeType value: {data!r}"
        )
    return cast(SearchContactsTimeRangeType, data)
