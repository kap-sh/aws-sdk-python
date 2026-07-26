"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchCollectionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.search_collection_type

SearchCollectionTypeList: TypeAlias = list[
    "capo_workdocs.types.search_collection_type.SearchCollectionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchCollectionTypeList) -> list:
    import capo_workdocs.types.search_collection_type

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.search_collection_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchCollectionTypeList:
    import capo_workdocs.types.search_collection_type

    out: SearchCollectionTypeList = []
    for item in data:
        out.append(capo_workdocs.types.search_collection_type.deserialize_json(item))
    return out
