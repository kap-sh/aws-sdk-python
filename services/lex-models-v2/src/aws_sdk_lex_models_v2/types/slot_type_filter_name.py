"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeFilterName``."""

from typing import Literal, TypeAlias, cast

SlotTypeFilterName: TypeAlias = Literal[
    "SlotTypeName",
    "ExternalSourceType",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeFilterName) -> str:
    return value


def deserialize_json(data: str) -> SlotTypeFilterName:
    return cast(SlotTypeFilterName, data)
