"""Generated from Smithy shape ``com.amazonaws.pcs#ComputeNodeGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pcs.types.ami_id
    import aws_sdk_pcs.types.compute_node_group_name
    import aws_sdk_pcs.types.compute_node_group_slurm_configuration
    import aws_sdk_pcs.types.compute_node_group_status
    import aws_sdk_pcs.types.custom_launch_template
    import aws_sdk_pcs.types.error_info_list
    import aws_sdk_pcs.types.instance_list
    import aws_sdk_pcs.types.instance_profile_arn
    import aws_sdk_pcs.types.purchase_option
    import aws_sdk_pcs.types.scaling_configuration
    import aws_sdk_pcs.types.spot_options
    import aws_sdk_pcs.types.subnet_id_list


class ComputeNodeGroup(TypedDict, closed=True):
    name: "aws_sdk_pcs.types.compute_node_group_name.ComputeNodeGroupName"
    """<p>The name that identifies the compute node group.</p>"""
    id: "str"
    """<p>The generated unique ID of the compute node group.</p>"""
    arn: "str"
    """<p>The unique Amazon Resource Name (ARN) of the compute node group.</p>"""
    cluster_id: "str"
    """<p>The ID of the cluster of the compute node group.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the resource was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the resource was modified.</p>"""
    status: "aws_sdk_pcs.types.compute_node_group_status.ComputeNodeGroupStatus"
    r"""<p>The provisioning status of the compute node group.</p> <note> <p>The provisioning status doesn't indicate the overall health of the compute node group.</p> </note> <important> <p>The resource enters the <code>SUSPENDING</code> and <code>SUSPENDED</code> states when the scheduler is beyond end of life and we have suspended the cluster. When in these states, you can't use the cluster. The cluster controller is down and all compute instances are terminated. The resources still count toward your service quotas. You can delete a resource if its status is <code>SUSPENDED</code>. For more information, see <a href=\"https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html\">Frequently asked questions about Slurm versions in PCS</a> in the <i>PCS User Guide</i>.</p> </important>"""
    ami_id: NotRequired["aws_sdk_pcs.types.ami_id.AmiId"]
    """<p>The ID of the Amazon Machine Image (AMI) that PCS uses to launch instances. If not provided, PCS uses the AMI ID specified in the custom launch template.</p>"""
    subnet_ids: "aws_sdk_pcs.types.subnet_id_list.SubnetIdList"
    """<p>The list of subnet IDs where instances are provisioned by the compute node group. The subnets must be in the same VPC as the cluster.</p>"""
    purchase_option: NotRequired["aws_sdk_pcs.types.purchase_option.PurchaseOption"]
    r"""<p>Specifies how EC2 instances are purchased on your behalf. PCS supports On-Demand Instances, Spot Instances, Interruptible Capacity Reservations, On-Demand Capacity Reservations, and Amazon EC2 Capacity Blocks for ML. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html\">Amazon EC2 billing and purchasing options</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. For more information about PCS support for Capacity Blocks, see <a href=\"https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks.html\">Using Amazon EC2 Capacity Blocks for ML with PCS</a> in the <i>PCS User Guide</i>. For more information about PCS support for interruptible capacity reservations, see <a href=\"https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-iodcr.html\">Using I-ODCRs with PCS</a> in the <i>PCS User Guide</i>. Choose On-Demand if you plan to use an On-Demand Capacity Reservation (ODCR). For more information, see <a href=\"https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-odcr.html\">Using ODCRs with PCS</a>. If you don't provide this option, it defaults to On-Demand.</p>"""
    custom_launch_template: (
        "aws_sdk_pcs.types.custom_launch_template.CustomLaunchTemplate"
    )
    iam_instance_profile_arn: (
        "aws_sdk_pcs.types.instance_profile_arn.InstanceProfileArn"
    )
    r"""<p>The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have the <code>pcs:RegisterComputeNodeGroupInstance</code> permission and the role name must start with <code>AWSPCS</code> or must have the path <code>/aws-pcs/</code>. For more information, see <a href=\"https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles.html\">IAM instance profiles for PCS</a> in the <i>PCS User Guide</i>.</p>"""
    scaling_configuration: (
        "aws_sdk_pcs.types.scaling_configuration.ScalingConfiguration"
    )
    instance_configs: "aws_sdk_pcs.types.instance_list.InstanceList"
    """<p>A list of EC2 instance configurations that PCS can provision in the compute node group.</p>"""
    spot_options: NotRequired["aws_sdk_pcs.types.spot_options.SpotOptions"]
    slurm_configuration: NotRequired[
        "aws_sdk_pcs.types.compute_node_group_slurm_configuration.ComputeNodeGroupSlurmConfiguration"
    ]
    error_info: NotRequired["aws_sdk_pcs.types.error_info_list.ErrorInfoList"]
    """<p>The list of errors that occurred during compute node group provisioning.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeNodeGroup) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["clusterId"] = value["cluster_id"]
    import aws_sdk_pcs.types._prelude.timestamp

    out["createdAt"] = aws_sdk_pcs.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import aws_sdk_pcs.types._prelude.timestamp

    out["modifiedAt"] = aws_sdk_pcs.types._prelude.timestamp.serialize_aws_json_1_0(
        value["modified_at"]
    )
    import aws_sdk_pcs.types.compute_node_group_status

    out["status"] = aws_sdk_pcs.types.compute_node_group_status.serialize_aws_json_1_0(
        value["status"]
    )
    if "ami_id" in value:
        out["amiId"] = value["ami_id"]
    import aws_sdk_pcs.types.subnet_id_list

    out["subnetIds"] = aws_sdk_pcs.types.subnet_id_list.serialize_aws_json_1_0(
        value["subnet_ids"]
    )
    if "purchase_option" in value:
        import aws_sdk_pcs.types.purchase_option

        out["purchaseOption"] = (
            aws_sdk_pcs.types.purchase_option.serialize_aws_json_1_0(
                value["purchase_option"]
            )
        )
    import aws_sdk_pcs.types.custom_launch_template

    out["customLaunchTemplate"] = (
        aws_sdk_pcs.types.custom_launch_template.serialize_aws_json_1_0(
            value["custom_launch_template"]
        )
    )
    out["iamInstanceProfileArn"] = value["iam_instance_profile_arn"]
    import aws_sdk_pcs.types.scaling_configuration

    out["scalingConfiguration"] = (
        aws_sdk_pcs.types.scaling_configuration.serialize_aws_json_1_0(
            value["scaling_configuration"]
        )
    )
    import aws_sdk_pcs.types.instance_list

    out["instanceConfigs"] = aws_sdk_pcs.types.instance_list.serialize_aws_json_1_0(
        value["instance_configs"]
    )
    if "spot_options" in value:
        import aws_sdk_pcs.types.spot_options

        out["spotOptions"] = aws_sdk_pcs.types.spot_options.serialize_aws_json_1_0(
            value["spot_options"]
        )
    if "slurm_configuration" in value:
        import aws_sdk_pcs.types.compute_node_group_slurm_configuration

        out["slurmConfiguration"] = (
            aws_sdk_pcs.types.compute_node_group_slurm_configuration.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    if "error_info" in value:
        import aws_sdk_pcs.types.error_info_list

        out["errorInfo"] = aws_sdk_pcs.types.error_info_list.serialize_aws_json_1_0(
            value["error_info"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ComputeNodeGroup:
    out: ComputeNodeGroup = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ComputeNodeGroup.name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ComputeNodeGroup.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ComputeNodeGroup.arn required")
    if "clusterId" in data:
        out["cluster_id"] = data["clusterId"]
    else:
        raise DeserializationError("ComputeNodeGroup.cluster_id required")
    if "createdAt" in data:
        import aws_sdk_pcs.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_pcs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ComputeNodeGroup.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_pcs.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_pcs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["modifiedAt"]
            )
        )
    else:
        raise DeserializationError("ComputeNodeGroup.modified_at required")
    if "status" in data:
        import aws_sdk_pcs.types.compute_node_group_status

        out["status"] = (
            aws_sdk_pcs.types.compute_node_group_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ComputeNodeGroup.status required")
    if "amiId" in data:
        out["ami_id"] = data["amiId"]
    if "subnetIds" in data:
        import aws_sdk_pcs.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_pcs.types.subnet_id_list.deserialize_aws_json_1_0(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("ComputeNodeGroup.subnet_ids required")
    if "purchaseOption" in data:
        import aws_sdk_pcs.types.purchase_option

        out["purchase_option"] = (
            aws_sdk_pcs.types.purchase_option.deserialize_aws_json_1_0(
                data["purchaseOption"]
            )
        )
    if "customLaunchTemplate" in data:
        import aws_sdk_pcs.types.custom_launch_template

        out["custom_launch_template"] = (
            aws_sdk_pcs.types.custom_launch_template.deserialize_aws_json_1_0(
                data["customLaunchTemplate"]
            )
        )
    else:
        raise DeserializationError("ComputeNodeGroup.custom_launch_template required")
    if "iamInstanceProfileArn" in data:
        out["iam_instance_profile_arn"] = data["iamInstanceProfileArn"]
    else:
        raise DeserializationError("ComputeNodeGroup.iam_instance_profile_arn required")
    if "scalingConfiguration" in data:
        import aws_sdk_pcs.types.scaling_configuration

        out["scaling_configuration"] = (
            aws_sdk_pcs.types.scaling_configuration.deserialize_aws_json_1_0(
                data["scalingConfiguration"]
            )
        )
    else:
        raise DeserializationError("ComputeNodeGroup.scaling_configuration required")
    if "instanceConfigs" in data:
        import aws_sdk_pcs.types.instance_list

        out["instance_configs"] = (
            aws_sdk_pcs.types.instance_list.deserialize_aws_json_1_0(
                data["instanceConfigs"]
            )
        )
    else:
        raise DeserializationError("ComputeNodeGroup.instance_configs required")
    if "spotOptions" in data:
        import aws_sdk_pcs.types.spot_options

        out["spot_options"] = aws_sdk_pcs.types.spot_options.deserialize_aws_json_1_0(
            data["spotOptions"]
        )
    if "slurmConfiguration" in data:
        import aws_sdk_pcs.types.compute_node_group_slurm_configuration

        out["slurm_configuration"] = (
            aws_sdk_pcs.types.compute_node_group_slurm_configuration.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if "errorInfo" in data:
        import aws_sdk_pcs.types.error_info_list

        out["error_info"] = aws_sdk_pcs.types.error_info_list.deserialize_aws_json_1_0(
            data["errorInfo"]
        )
    return out
