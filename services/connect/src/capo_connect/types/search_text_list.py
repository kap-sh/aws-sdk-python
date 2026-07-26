"""Generated from Smithy shape ``com.amazonaws.connect#SearchTextList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.search_text

SearchTextList: TypeAlias = list["capo_connect.types.search_text.SearchText"]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextList) -> list:
    return list(value)


def deserialize_json(data: list) -> SearchTextList:
    return list(data)
