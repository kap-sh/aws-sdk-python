"""Generated from Smithy shape ``com.amazonaws.glue#PrincipalPermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.principal_permissions

PrincipalPermissionsList: TypeAlias = list[
    "aws_sdk_glue.types.principal_permissions.PrincipalPermissions"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrincipalPermissionsList) -> list:
    import aws_sdk_glue.types.principal_permissions

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.principal_permissions.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PrincipalPermissionsList:
    import aws_sdk_glue.types.principal_permissions

    out: PrincipalPermissionsList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.principal_permissions.deserialize_aws_json_1_1(item)
        )
    return out
