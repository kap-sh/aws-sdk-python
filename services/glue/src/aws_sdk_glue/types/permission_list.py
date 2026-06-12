"""Generated from Smithy shape ``com.amazonaws.glue#PermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.permission

PermissionList: TypeAlias = list["aws_sdk_glue.types.permission.Permission"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionList) -> list:
    import aws_sdk_glue.types.permission

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.permission.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PermissionList:
    import aws_sdk_glue.types.permission

    out: PermissionList = []
    for item in data:
        out.append(aws_sdk_glue.types.permission.deserialize_aws_json_1_1(item))
    return out
