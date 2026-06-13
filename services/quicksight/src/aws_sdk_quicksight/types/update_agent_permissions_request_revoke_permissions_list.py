"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAgentPermissionsRequestRevokePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.resource_permission

UpdateAgentPermissionsRequestRevokePermissionsList: TypeAlias = list[
    "aws_sdk_quicksight.types.resource_permission.ResourcePermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentPermissionsRequestRevokePermissionsList) -> list:
    import aws_sdk_quicksight.types.resource_permission

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.resource_permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateAgentPermissionsRequestRevokePermissionsList:
    import aws_sdk_quicksight.types.resource_permission

    out: UpdateAgentPermissionsRequestRevokePermissionsList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.resource_permission.deserialize_json(item))
    return out
