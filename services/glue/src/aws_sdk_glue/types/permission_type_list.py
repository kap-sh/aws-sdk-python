"""Generated from Smithy shape ``com.amazonaws.glue#PermissionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.permission_type

PermissionTypeList: TypeAlias = list[
    "aws_sdk_glue.types.permission_type.PermissionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionTypeList) -> list:
    import aws_sdk_glue.types.permission_type

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.permission_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PermissionTypeList:
    import aws_sdk_glue.types.permission_type

    out: PermissionTypeList = []
    for item in data:
        out.append(aws_sdk_glue.types.permission_type.deserialize_aws_json_1_1(item))
    return out
