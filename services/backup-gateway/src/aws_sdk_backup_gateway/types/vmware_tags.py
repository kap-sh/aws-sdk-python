"""Generated from Smithy shape ``com.amazonaws.backupgateway#VmwareTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.vmware_tag

VmwareTags: TypeAlias = list["aws_sdk_backup_gateway.types.vmware_tag.VmwareTag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VmwareTags) -> list:
    import aws_sdk_backup_gateway.types.vmware_tag

    out: list = []
    for item in value:
        out.append(aws_sdk_backup_gateway.types.vmware_tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> VmwareTags:
    import aws_sdk_backup_gateway.types.vmware_tag

    out: VmwareTags = []
    for item in data:
        out.append(
            aws_sdk_backup_gateway.types.vmware_tag.deserialize_aws_json_1_0(item)
        )
    return out
