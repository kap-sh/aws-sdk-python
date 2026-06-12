"""Generated from Smithy shape ``com.amazonaws.cloud9#PermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.permissions

PermissionsList: TypeAlias = list["aws_sdk_cloud9.types.permissions.Permissions"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionsList) -> list:
    import aws_sdk_cloud9.types.permissions

    out: list = []
    for item in value:
        out.append(aws_sdk_cloud9.types.permissions.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PermissionsList:
    import aws_sdk_cloud9.types.permissions

    out: PermissionsList = []
    for item in data:
        out.append(aws_sdk_cloud9.types.permissions.deserialize_aws_json_1_1(item))
    return out
