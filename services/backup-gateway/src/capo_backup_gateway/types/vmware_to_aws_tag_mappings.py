"""Generated from Smithy shape ``com.amazonaws.backupgateway#VmwareToAwsTagMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup_gateway.types.vmware_to_aws_tag_mapping

VmwareToAwsTagMappings: TypeAlias = list[
    "capo_backup_gateway.types.vmware_to_aws_tag_mapping.VmwareToAwsTagMapping"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VmwareToAwsTagMappings) -> list:
    import capo_backup_gateway.types.vmware_to_aws_tag_mapping

    out: list = []
    for item in value:
        out.append(
            capo_backup_gateway.types.vmware_to_aws_tag_mapping.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VmwareToAwsTagMappings:
    import capo_backup_gateway.types.vmware_to_aws_tag_mapping

    out: VmwareToAwsTagMappings = []
    for item in data:
        out.append(
            capo_backup_gateway.types.vmware_to_aws_tag_mapping.deserialize_aws_json_1_0(
                item
            )
        )
    return out
