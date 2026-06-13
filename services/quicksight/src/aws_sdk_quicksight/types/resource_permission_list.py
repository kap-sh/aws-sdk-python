"""Generated from Smithy shape ``com.amazonaws.quicksight#ResourcePermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.resource_permission

ResourcePermissionList: TypeAlias = list[
    "aws_sdk_quicksight.types.resource_permission.ResourcePermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePermissionList) -> list:
    import aws_sdk_quicksight.types.resource_permission

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.resource_permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourcePermissionList:
    import aws_sdk_quicksight.types.resource_permission

    out: ResourcePermissionList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.resource_permission.deserialize_json(item))
    return out
