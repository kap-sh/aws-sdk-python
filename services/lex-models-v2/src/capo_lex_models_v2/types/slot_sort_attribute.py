"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotSortAttribute``."""

from typing import Literal, TypeAlias, cast

SlotSortAttribute: TypeAlias = Literal[
    "SlotName",
    "LastUpdatedDateTime",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> SlotSortAttribute:
    return cast(SlotSortAttribute, data)
