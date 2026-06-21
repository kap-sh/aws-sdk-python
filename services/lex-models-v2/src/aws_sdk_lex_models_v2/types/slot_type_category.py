"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotTypeCategory``."""

from typing import Literal, TypeAlias, cast

SlotTypeCategory: TypeAlias = Literal[
    "Custom",
    "Extended",
    "ExternalGrammar",
    "Composite",
]


# --- restJson1 ser/de ---
def serialize_json(value: SlotTypeCategory) -> str:
    return value


def deserialize_json(data: str) -> SlotTypeCategory:
    return cast(SlotTypeCategory, data)
