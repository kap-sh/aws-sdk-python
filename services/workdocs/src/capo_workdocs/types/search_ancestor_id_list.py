"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchAncestorIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.search_ancestor_id

SearchAncestorIdList: TypeAlias = list[
    "capo_workdocs.types.search_ancestor_id.SearchAncestorId"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchAncestorIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SearchAncestorIdList:
    return list(data)
