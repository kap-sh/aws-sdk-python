"""Generated from Smithy shape ``com.amazonaws.datazone#TextMatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.text_match_item

TextMatches: TypeAlias = list["capo_datazone.types.text_match_item.TextMatchItem"]


# --- restJson1 ser/de ---
def serialize_json(value: TextMatches) -> list:
    import capo_datazone.types.text_match_item

    out: list = []
    for item in value:
        out.append(capo_datazone.types.text_match_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> TextMatches:
    import capo_datazone.types.text_match_item

    out: TextMatches = []
    for item in data:
        out.append(capo_datazone.types.text_match_item.deserialize_json(item))
    return out
