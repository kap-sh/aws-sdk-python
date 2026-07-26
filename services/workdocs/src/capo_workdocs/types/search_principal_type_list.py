"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchPrincipalTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.search_principal_type

SearchPrincipalTypeList: TypeAlias = list[
    "capo_workdocs.types.search_principal_type.SearchPrincipalType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchPrincipalTypeList) -> list:
    import capo_workdocs.types.search_principal_type

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.search_principal_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchPrincipalTypeList:
    import capo_workdocs.types.search_principal_type

    out: SearchPrincipalTypeList = []
    for item in data:
        out.append(capo_workdocs.types.search_principal_type.deserialize_json(item))
    return out
