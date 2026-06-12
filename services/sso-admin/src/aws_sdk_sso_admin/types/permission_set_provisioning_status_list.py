"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PermissionSetProvisioningStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.permission_set_provisioning_status_metadata

PermissionSetProvisioningStatusList: TypeAlias = list[
    "aws_sdk_sso_admin.types.permission_set_provisioning_status_metadata.PermissionSetProvisioningStatusMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PermissionSetProvisioningStatusList) -> list:
    import aws_sdk_sso_admin.types.permission_set_provisioning_status_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sso_admin.types.permission_set_provisioning_status_metadata.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PermissionSetProvisioningStatusList:
    import aws_sdk_sso_admin.types.permission_set_provisioning_status_metadata

    out: PermissionSetProvisioningStatusList = []
    for item in data:
        out.append(
            aws_sdk_sso_admin.types.permission_set_provisioning_status_metadata.deserialize_aws_json_1_1(
                item
            )
        )
    return out
