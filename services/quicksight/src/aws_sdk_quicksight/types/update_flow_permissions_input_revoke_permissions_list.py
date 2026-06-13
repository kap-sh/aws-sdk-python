"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFlowPermissionsInputRevokePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.permission

UpdateFlowPermissionsInputRevokePermissionsList: TypeAlias = list[
    "aws_sdk_quicksight.types.permission.Permission"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowPermissionsInputRevokePermissionsList) -> list:
    import aws_sdk_quicksight.types.permission

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateFlowPermissionsInputRevokePermissionsList:
    import aws_sdk_quicksight.types.permission

    out: UpdateFlowPermissionsInputRevokePermissionsList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.permission.deserialize_json(item))
    return out
