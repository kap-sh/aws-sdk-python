"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.search_resource_type

SearchResourceTypeList: TypeAlias = list[
    "capo_workdocs.types.search_resource_type.SearchResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourceTypeList) -> list:
    import capo_workdocs.types.search_resource_type

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.search_resource_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchResourceTypeList:
    import capo_workdocs.types.search_resource_type

    out: SearchResourceTypeList = []
    for item in data:
        out.append(capo_workdocs.types.search_resource_type.deserialize_json(item))
    return out
