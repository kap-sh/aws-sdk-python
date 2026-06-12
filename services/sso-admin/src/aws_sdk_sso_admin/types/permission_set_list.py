"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PermissionSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.permission_set_arn

PermissionSetList: TypeAlias = list[
    "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionSetList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PermissionSetList:
    return list(data)
