"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingLaunchConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_list
    import capo_securityhub.types.aws_auto_scaling_launch_configuration_instance_monitoring_details
    import capo_securityhub.types.aws_auto_scaling_launch_configuration_metadata_options
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsAutoScalingLaunchConfigurationDetails(TypedDict, closed=True):
    associate_public_ip_address: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>For Auto Scaling groups that run in a VPC, specifies whether to assign a public IP address to the group's instances.</p>"""
    block_device_mappings: NotRequired[
        "capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_list.AwsAutoScalingLaunchConfigurationBlockDeviceMappingsList"
    ]
    """<p>Specifies the block devices for the instance.</p>"""
    classic_link_vpc_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of a ClassicLink-enabled VPC that EC2-Classic instances are linked to.</p>"""
    classic_link_vpc_security_groups: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The identifiers of one or more security groups for the VPC that is specified in <code>ClassicLinkVPCId</code>.</p>"""
    created_time: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    r"""<p>The creation date and time for the launch configuration.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    ebs_optimized: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the launch configuration is optimized for Amazon EBS I/O.</p>"""
    iam_instance_profile: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name or the ARN of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role.</p>"""
    image_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the Amazon Machine Image (AMI) that is used to launch EC2 instances.</p>"""
    instance_monitoring: NotRequired[
        "capo_securityhub.types.aws_auto_scaling_launch_configuration_instance_monitoring_details.AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails"
    ]
    """<p>Indicates the type of monitoring for instances in the group.</p>"""
    instance_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The instance type for the instances.</p>"""
    kernel_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the kernel associated with the AMI.</p>"""
    key_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the key pair.</p>"""
    launch_configuration_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the launch configuration.</p>"""
    placement_tenancy: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The tenancy of the instance. An instance with <code>dedicated</code> tenancy runs on isolated, single-tenant hardware and can only be launched into a VPC.</p>"""
    ramdisk_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the RAM disk associated with the AMI.</p>"""
    security_groups: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The security groups to assign to the instances in the Auto Scaling group.</p>"""
    spot_price: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The maximum hourly price to be paid for any Spot Instance that is launched to fulfill the request.</p>"""
    user_data: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The user data to make available to the launched EC2 instances. Must be base64-encoded text.</p>"""
    metadata_options: NotRequired[
        "capo_securityhub.types.aws_auto_scaling_launch_configuration_metadata_options.AwsAutoScalingLaunchConfigurationMetadataOptions"
    ]
    """<p>The metadata options for the instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAutoScalingLaunchConfigurationDetails) -> dict:
    out: dict = {}
    if "associate_public_ip_address" in value:
        out["AssociatePublicIpAddress"] = value["associate_public_ip_address"]
    if "block_device_mappings" in value:
        import capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_list

        out["BlockDeviceMappings"] = (
            capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_list.serialize_json(
                value["block_device_mappings"]
            )
        )
    if "classic_link_vpc_id" in value:
        out["ClassicLinkVpcId"] = value["classic_link_vpc_id"]
    if "classic_link_vpc_security_groups" in value:
        import capo_securityhub.types.non_empty_string_list

        out["ClassicLinkVpcSecurityGroups"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["classic_link_vpc_security_groups"]
            )
        )
    if "created_time" in value:
        out["CreatedTime"] = value["created_time"]
    if "ebs_optimized" in value:
        out["EbsOptimized"] = value["ebs_optimized"]
    if "iam_instance_profile" in value:
        out["IamInstanceProfile"] = value["iam_instance_profile"]
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "instance_monitoring" in value:
        import capo_securityhub.types.aws_auto_scaling_launch_configuration_instance_monitoring_details

        out["InstanceMonitoring"] = (
            capo_securityhub.types.aws_auto_scaling_launch_configuration_instance_monitoring_details.serialize_json(
                value["instance_monitoring"]
            )
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "kernel_id" in value:
        out["KernelId"] = value["kernel_id"]
    if "key_name" in value:
        out["KeyName"] = value["key_name"]
    if "launch_configuration_name" in value:
        out["LaunchConfigurationName"] = value["launch_configuration_name"]
    if "placement_tenancy" in value:
        out["PlacementTenancy"] = value["placement_tenancy"]
    if "ramdisk_id" in value:
        out["RamdiskId"] = value["ramdisk_id"]
    if "security_groups" in value:
        import capo_securityhub.types.non_empty_string_list

        out["SecurityGroups"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["security_groups"]
            )
        )
    if "spot_price" in value:
        out["SpotPrice"] = value["spot_price"]
    if "user_data" in value:
        out["UserData"] = value["user_data"]
    if "metadata_options" in value:
        import capo_securityhub.types.aws_auto_scaling_launch_configuration_metadata_options

        out["MetadataOptions"] = (
            capo_securityhub.types.aws_auto_scaling_launch_configuration_metadata_options.serialize_json(
                value["metadata_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsAutoScalingLaunchConfigurationDetails:
    out: AwsAutoScalingLaunchConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "AssociatePublicIpAddress" in data:
        out["associate_public_ip_address"] = data["AssociatePublicIpAddress"]
    if "BlockDeviceMappings" in data:
        import capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_list

        out["block_device_mappings"] = (
            capo_securityhub.types.aws_auto_scaling_launch_configuration_block_device_mappings_list.deserialize_json(
                data["BlockDeviceMappings"]
            )
        )
    if "ClassicLinkVpcId" in data:
        out["classic_link_vpc_id"] = data["ClassicLinkVpcId"]
    if "ClassicLinkVpcSecurityGroups" in data:
        import capo_securityhub.types.non_empty_string_list

        out["classic_link_vpc_security_groups"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["ClassicLinkVpcSecurityGroups"]
            )
        )
    if "CreatedTime" in data:
        out["created_time"] = data["CreatedTime"]
    if "EbsOptimized" in data:
        out["ebs_optimized"] = data["EbsOptimized"]
    if "IamInstanceProfile" in data:
        out["iam_instance_profile"] = data["IamInstanceProfile"]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    if "InstanceMonitoring" in data:
        import capo_securityhub.types.aws_auto_scaling_launch_configuration_instance_monitoring_details

        out["instance_monitoring"] = (
            capo_securityhub.types.aws_auto_scaling_launch_configuration_instance_monitoring_details.deserialize_json(
                data["InstanceMonitoring"]
            )
        )
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "KernelId" in data:
        out["kernel_id"] = data["KernelId"]
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    if "LaunchConfigurationName" in data:
        out["launch_configuration_name"] = data["LaunchConfigurationName"]
    if "PlacementTenancy" in data:
        out["placement_tenancy"] = data["PlacementTenancy"]
    if "RamdiskId" in data:
        out["ramdisk_id"] = data["RamdiskId"]
    if "SecurityGroups" in data:
        import capo_securityhub.types.non_empty_string_list

        out["security_groups"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["SecurityGroups"]
            )
        )
    if "SpotPrice" in data:
        out["spot_price"] = data["SpotPrice"]
    if "UserData" in data:
        out["user_data"] = data["UserData"]
    if "MetadataOptions" in data:
        import capo_securityhub.types.aws_auto_scaling_launch_configuration_metadata_options

        out["metadata_options"] = (
            capo_securityhub.types.aws_auto_scaling_launch_configuration_metadata_options.deserialize_json(
                data["MetadataOptions"]
            )
        )
    return out
