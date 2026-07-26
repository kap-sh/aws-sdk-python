"""Generated from Smithy shape ``com.amazonaws.glue#PermissionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.permission_type

PermissionTypeList: TypeAlias = list["capo_glue.types.permission_type.PermissionType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionTypeList) -> list:
    import capo_glue.types.permission_type

    out: list = []
    for item in value:
        out.append(capo_glue.types.permission_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PermissionTypeList:
    import capo_glue.types.permission_type

    out: PermissionTypeList = []
    for item in data:
        out.append(capo_glue.types.permission_type.deserialize_aws_json_1_1(item))
    return out
