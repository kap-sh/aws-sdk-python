"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasPermissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.connection_alias_permission

ConnectionAliasPermissions: TypeAlias = list[
    "aws_sdk_workspaces.types.connection_alias_permission.ConnectionAliasPermission"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasPermissions) -> list:
    import aws_sdk_workspaces.types.connection_alias_permission

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.connection_alias_permission.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionAliasPermissions:
    import aws_sdk_workspaces.types.connection_alias_permission

    out: ConnectionAliasPermissions = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.connection_alias_permission.deserialize_aws_json_1_1(
                item
            )
        )
    return out
