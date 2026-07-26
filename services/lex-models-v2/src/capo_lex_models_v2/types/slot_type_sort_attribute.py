"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeSortAttribute``."""

from typing import Literal, TypeAlias, cast

SlotTypeSortAttribute: TypeAlias = Literal[
    "SlotTypeName",
    "LastUpdatedDateTime",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> SlotTypeSortAttribute:
    return cast(SlotTypeSortAttribute, data)
