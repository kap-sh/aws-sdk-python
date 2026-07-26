"""Generated from Smithy shape ``com.amazonaws.lakeformation#PrincipalPermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.principal_permissions

PrincipalPermissionsList: TypeAlias = list[
    "capo_lakeformation.types.principal_permissions.PrincipalPermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalPermissionsList) -> list:
    import capo_lakeformation.types.principal_permissions

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.principal_permissions.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrincipalPermissionsList:
    import capo_lakeformation.types.principal_permissions

    out: PrincipalPermissionsList = []
    for item in data:
        out.append(
            capo_lakeformation.types.principal_permissions.deserialize_json(item)
        )
    return out
