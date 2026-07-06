"""Generated from Smithy shape ``com.amazonaws.backupgateway#GetHypervisorPropertyMappingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.iam_role_arn
    import aws_sdk_backup_gateway.types.server_arn
    import aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings


class GetHypervisorPropertyMappingsOutput(TypedDict, closed=True):
    hypervisor_arn: NotRequired["aws_sdk_backup_gateway.types.server_arn.ServerArn"]
    """<p>The Amazon Resource Name (ARN) of the hypervisor.</p>"""
    vmware_to_aws_tag_mappings: NotRequired[
        "aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings.VmwareToAwsTagMappings"
    ]
    """<p>This is a display of the mappings of VMware tags to the Amazon Web Services tags.</p>"""
    iam_role_arn: NotRequired["aws_sdk_backup_gateway.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetHypervisorPropertyMappingsOutput) -> dict:
    out: dict = {}
    if "hypervisor_arn" in value:
        out["HypervisorArn"] = value["hypervisor_arn"]
    if "vmware_to_aws_tag_mappings" in value:
        import aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings

        out["VmwareToAwsTagMappings"] = (
            aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings.serialize_aws_json_1_0(
                value["vmware_to_aws_tag_mappings"]
            )
        )
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetHypervisorPropertyMappingsOutput:
    out: GetHypervisorPropertyMappingsOutput = {}  # type: ignore[typeddict-item]
    if "HypervisorArn" in data:
        out["hypervisor_arn"] = data["HypervisorArn"]
    if "VmwareToAwsTagMappings" in data:
        import aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings

        out["vmware_to_aws_tag_mappings"] = (
            aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings.deserialize_aws_json_1_0(
                data["VmwareToAwsTagMappings"]
            )
        )
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    return out
