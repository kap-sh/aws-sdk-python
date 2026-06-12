"""Generated from Smithy shape ``com.amazonaws.connect#SortableFieldName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

SortableFieldName: TypeAlias = Literal[
    "INITIATION_TIMESTAMP",
    "SCHEDULED_TIMESTAMP",
    "CONNECTED_TO_AGENT_TIMESTAMP",
    "DISCONNECT_TIMESTAMP",
    "INITIATION_METHOD",
    "CHANNEL",
    "EXPIRY_TIMESTAMP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIATION_TIMESTAMP",
        "SCHEDULED_TIMESTAMP",
        "CONNECTED_TO_AGENT_TIMESTAMP",
        "DISCONNECT_TIMESTAMP",
        "INITIATION_METHOD",
        "CHANNEL",
        "EXPIRY_TIMESTAMP",
    )
)


def serialize_json(value: SortableFieldName) -> str:
    return value


def deserialize_json(data: str) -> SortableFieldName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortableFieldName value: {data!r}")
    return cast(SortableFieldName, data)
