"""Generated from Smithy shape ``com.amazonaws.backupgateway#PutHypervisorPropertyMappingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.iam_role_arn
    import aws_sdk_backup_gateway.types.server_arn
    import aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings


class PutHypervisorPropertyMappingsInput(TypedDict, closed=True):
    hypervisor_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn"
    """<p>The Amazon Resource Name (ARN) of the hypervisor.</p>"""
    vmware_to_aws_tag_mappings: (
        "aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings.VmwareToAwsTagMappings"
    )
    """<p>This action requests the mappings of VMware tags to the Amazon Web Services tags.</p>"""
    iam_role_arn: "aws_sdk_backup_gateway.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutHypervisorPropertyMappingsInput) -> dict:
    out: dict = {}
    out["HypervisorArn"] = value["hypervisor_arn"]
    import aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings

    out["VmwareToAwsTagMappings"] = (
        aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings.serialize_aws_json_1_0(
            value["vmware_to_aws_tag_mappings"]
        )
    )
    out["IamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutHypervisorPropertyMappingsInput:
    out: PutHypervisorPropertyMappingsInput = {}  # type: ignore[typeddict-item]
    if "HypervisorArn" in data:
        out["hypervisor_arn"] = data["HypervisorArn"]
    else:
        raise DeserializationError(
            "PutHypervisorPropertyMappingsInput.hypervisor_arn required"
        )
    if "VmwareToAwsTagMappings" in data:
        import aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings

        out["vmware_to_aws_tag_mappings"] = (
            aws_sdk_backup_gateway.types.vmware_to_aws_tag_mappings.deserialize_aws_json_1_0(
                data["VmwareToAwsTagMappings"]
            )
        )
    else:
        raise DeserializationError(
            "PutHypervisorPropertyMappingsInput.vmware_to_aws_tag_mappings required"
        )
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError(
            "PutHypervisorPropertyMappingsInput.iam_role_arn required"
        )
    return out
