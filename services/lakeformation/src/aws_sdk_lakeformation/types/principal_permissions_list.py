"""Generated from Smithy shape ``com.amazonaws.lakeformation#PrincipalPermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.principal_permissions

PrincipalPermissionsList: TypeAlias = list[
    "aws_sdk_lakeformation.types.principal_permissions.PrincipalPermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalPermissionsList) -> list:
    import aws_sdk_lakeformation.types.principal_permissions

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lakeformation.types.principal_permissions.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PrincipalPermissionsList:
    import aws_sdk_lakeformation.types.principal_permissions

    out: PrincipalPermissionsList = []
    for item in data:
        out.append(
            aws_sdk_lakeformation.types.principal_permissions.deserialize_json(item)
        )
    return out
