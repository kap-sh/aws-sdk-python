"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchLabelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.search_label

SearchLabelList: TypeAlias = list["capo_workdocs.types.search_label.SearchLabel"]


# --- restJson1 ser/de ---
def serialize_json(value: SearchLabelList) -> list:
    return list(value)


def deserialize_json(data: list) -> SearchLabelList:
    return list(data)
