"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchQueryScopeTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.search_query_scope_type

SearchQueryScopeTypeList: TypeAlias = list[
    "capo_workdocs.types.search_query_scope_type.SearchQueryScopeType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchQueryScopeTypeList) -> list:
    import capo_workdocs.types.search_query_scope_type

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.search_query_scope_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchQueryScopeTypeList:
    import capo_workdocs.types.search_query_scope_type

    out: SearchQueryScopeTypeList = []
    for item in data:
        out.append(capo_workdocs.types.search_query_scope_type.deserialize_json(item))
    return out
