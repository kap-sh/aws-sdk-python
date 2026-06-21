"""Generated from Smithy shape ``com.amazonaws.connectparticipant#SortKey``."""

from typing import Literal, TypeAlias, cast

SortKey: TypeAlias = Literal[
    "DESCENDING",
    "ASCENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: SortKey) -> str:
    return value


def deserialize_json(data: str) -> SortKey:
    return cast(SortKey, data)
