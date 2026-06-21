"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsTimeRangeType``."""

from typing import Literal, TypeAlias, cast

SearchContactsTimeRangeType: TypeAlias = Literal[
    "INITIATION_TIMESTAMP",
    "SCHEDULED_TIMESTAMP",
    "CONNECTED_TO_AGENT_TIMESTAMP",
    "DISCONNECT_TIMESTAMP",
    "ENQUEUE_TIMESTAMP",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsTimeRangeType) -> str:
    return value


def deserialize_json(data: str) -> SearchContactsTimeRangeType:
    return cast(SearchContactsTimeRangeType, data)
