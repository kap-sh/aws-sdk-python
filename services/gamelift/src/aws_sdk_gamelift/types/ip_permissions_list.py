"""Generated from Smithy shape ``com.amazonaws.gamelift#IpPermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.ip_permission

IpPermissionsList: TypeAlias = list["aws_sdk_gamelift.types.ip_permission.IpPermission"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpPermissionsList) -> list:
    import aws_sdk_gamelift.types.ip_permission

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.ip_permission.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IpPermissionsList:
    import aws_sdk_gamelift.types.ip_permission

    out: IpPermissionsList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.ip_permission.deserialize_aws_json_1_1(item))
    return out
