"""Generated from Smithy shape ``com.amazonaws.quicksight#Synonyms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string

Synonyms: TypeAlias = list["capo_quicksight.types.limited_string.LimitedString"]


# --- restJson1 ser/de ---
def serialize_json(value: Synonyms) -> list:
    return list(value)


def deserialize_json(data: list) -> Synonyms:
    return list(data)
