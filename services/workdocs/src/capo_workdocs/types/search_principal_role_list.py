"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchPrincipalRoleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.principal_role_type

SearchPrincipalRoleList: TypeAlias = list[
    "capo_workdocs.types.principal_role_type.PrincipalRoleType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchPrincipalRoleList) -> list:
    import capo_workdocs.types.principal_role_type

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.principal_role_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchPrincipalRoleList:
    import capo_workdocs.types.principal_role_type

    out: SearchPrincipalRoleList = []
    for item in data:
        out.append(capo_workdocs.types.principal_role_type.deserialize_json(item))
    return out
