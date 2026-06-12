"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchQueryScopeTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.search_query_scope_type

SearchQueryScopeTypeList: TypeAlias = list[
    "aws_sdk_workdocs.types.search_query_scope_type.SearchQueryScopeType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchQueryScopeTypeList) -> list:
    import aws_sdk_workdocs.types.search_query_scope_type

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.search_query_scope_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchQueryScopeTypeList:
    import aws_sdk_workdocs.types.search_query_scope_type

    out: SearchQueryScopeTypeList = []
    for item in data:
        out.append(
            aws_sdk_workdocs.types.search_query_scope_type.deserialize_json(item)
        )
    return out
