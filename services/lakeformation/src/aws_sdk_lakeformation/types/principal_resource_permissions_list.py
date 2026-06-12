"""Generated from Smithy shape ``com.amazonaws.lakeformation#PrincipalResourcePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.principal_resource_permissions

PrincipalResourcePermissionsList: TypeAlias = list[
    "aws_sdk_lakeformation.types.principal_resource_permissions.PrincipalResourcePermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalResourcePermissionsList) -> list:
    import aws_sdk_lakeformation.types.principal_resource_permissions

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lakeformation.types.principal_resource_permissions.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PrincipalResourcePermissionsList:
    import aws_sdk_lakeformation.types.principal_resource_permissions

    out: PrincipalResourcePermissionsList = []
    for item in data:
        out.append(
            aws_sdk_lakeformation.types.principal_resource_permissions.deserialize_json(
                item
            )
        )
    return out
