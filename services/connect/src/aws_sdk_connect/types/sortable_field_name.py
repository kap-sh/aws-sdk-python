"""Generated from Smithy shape ``com.amazonaws.connect#SortableFieldName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: SortableFieldName) -> str:
    return value


def deserialize_json(data: str) -> SortableFieldName:
    return cast(SortableFieldName, data)
