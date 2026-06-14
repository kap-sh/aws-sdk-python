"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_list
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_cpu_options_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_credit_specification_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_gpu_specification_set_list
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_list
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_enclave_options_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_hibernation_options_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_iam_instance_profile_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_market_options_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_requirements_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_license_set_list
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_maintenance_options_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_metadata_options_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_monitoring_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_list
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_placement_details
    import aws_sdk_securityhub.types.aws_ec2_launch_template_data_private_dns_name_options_details
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsEc2LaunchTemplateDataDetails(TypedDict):
    block_device_mapping_set: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_list.AwsEc2LaunchTemplateDataBlockDeviceMappingSetList"
    ]
    """<p> Information about a block device mapping for an Amazon EC2 launch template. </p>"""
    capacity_reservation_specification: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_details.AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails"
    ]
    """<p> Specifies an instance's Capacity Reservation targeting option. You can specify only one option at a time. </p>"""
    cpu_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_cpu_options_details.AwsEc2LaunchTemplateDataCpuOptionsDetails"
    ]
    r"""<p> Specifies the CPU options for an instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html\">Optimize CPU options</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. </p>"""
    credit_specification: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_credit_specification_details.AwsEc2LaunchTemplateDataCreditSpecificationDetails"
    ]
    """<p> Specifies the credit option for CPU usage of a T2, T3, or T3a instance. </p>"""
    disable_api_stop: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    r"""<p> Indicates whether to enable the instance for stop protection. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html#Using_StopProtection\">Enable stop protection</a> in the <i>Amazon EC2 User Guide</i>. </p>"""
    disable_api_termination: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> If you set this parameter to <code>true</code>, you can't terminate the instance using the Amazon EC2 console, CLI, or API. If set to <code>true</code>, you can. </p>"""
    ebs_optimized: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether the instance is optimized for Amazon EBS I/O. </p>"""
    elastic_gpu_specification_set: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_gpu_specification_set_list.AwsEc2LaunchTemplateDataElasticGpuSpecificationSetList"
    ]
    """<p> Provides details about Elastic Graphics accelerators to associate with the instance. </p>"""
    elastic_inference_accelerator_set: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_list.AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetList"
    ]
    """<p> The Amazon Elastic Inference accelerator for the instance. </p>"""
    enclave_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_enclave_options_details.AwsEc2LaunchTemplateDataEnclaveOptionsDetails"
    ]
    """<p> Indicates whether the Amazon EC2 instance is enabled for Amazon Web Services Nitro Enclaves. </p>"""
    hibernation_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_hibernation_options_details.AwsEc2LaunchTemplateDataHibernationOptionsDetails"
    ]
    """<p> Specifies whether your Amazon EC2 instance is configured for hibernation. </p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_iam_instance_profile_details.AwsEc2LaunchTemplateDataIamInstanceProfileDetails"
    ]
    """<p> The name or Amazon Resource Name (ARN) of an IAM instance profile. </p>"""
    image_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the Amazon Machine Image (AMI). </p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Provides the options for specifying the instance initiated shutdown behavior. </p>"""
    instance_market_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_market_options_details.AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails"
    ]
    """<p> Specifies the market (purchasing) option for an instance. </p>"""
    instance_requirements: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_requirements_details.AwsEc2LaunchTemplateDataInstanceRequirementsDetails"
    ]
    """<p> The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with these attributes. If you specify <code>InstanceRequirements</code>, you can't specify <code>InstanceType</code>. </p>"""
    instance_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p> The instance type. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html\">Instance types</a> in the <i>Amazon EC2 User Guide</i>. If you specify <code>InstanceType</code>, you can't specify <code>InstanceRequirements</code>. </p>"""
    kernel_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the kernel. </p>"""
    key_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the key pair that allows users to connect to the instance. </p>"""
    license_set: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_license_set_list.AwsEc2LaunchTemplateDataLicenseSetList"
    ]
    """<p> Specifies a license configuration for an instance. </p>"""
    maintenance_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_maintenance_options_details.AwsEc2LaunchTemplateDataMaintenanceOptionsDetails"
    ]
    """<p> The maintenance options of your instance. </p>"""
    metadata_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_metadata_options_details.AwsEc2LaunchTemplateDataMetadataOptionsDetails"
    ]
    r"""<p> The metadata options for the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html\">Instance metadata and user data</a> in the <i>Amazon EC2 User Guide</i>. </p>"""
    monitoring: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_monitoring_details.AwsEc2LaunchTemplateDataMonitoringDetails"
    ]
    """<p> The monitoring for the instance. </p>"""
    network_interface_set: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_list.AwsEc2LaunchTemplateDataNetworkInterfaceSetList"
    ]
    """<p> Specifies the parameters for a network interface that is attached to the instance. </p>"""
    placement: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_placement_details.AwsEc2LaunchTemplateDataPlacementDetails"
    ]
    """<p> Specifies the placement of an instance. </p>"""
    private_dns_name_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_launch_template_data_private_dns_name_options_details.AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails"
    ]
    """<p> The options for the instance hostname. </p>"""
    ram_disk_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the RAM disk. </p>"""
    security_group_id_set: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> One or more security group IDs. </p>"""
    security_group_set: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> One or more security group names. For a nondefault VPC, you must use security group IDs instead. You cannot specify both a security group ID and security name in the same request. </p>"""
    user_data: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The user data to make available to the instance. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataDetails) -> dict:
    out: dict = {}
    if "block_device_mapping_set" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_list

        out["BlockDeviceMappingSet"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_list.serialize_json(
                value["block_device_mapping_set"]
            )
        )
    if "capacity_reservation_specification" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_details

        out["CapacityReservationSpecification"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_details.serialize_json(
                value["capacity_reservation_specification"]
            )
        )
    if "cpu_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_cpu_options_details

        out["CpuOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_cpu_options_details.serialize_json(
                value["cpu_options"]
            )
        )
    if "credit_specification" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_credit_specification_details

        out["CreditSpecification"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_credit_specification_details.serialize_json(
                value["credit_specification"]
            )
        )
    if "disable_api_stop" in value:
        out["DisableApiStop"] = value["disable_api_stop"]
    if "disable_api_termination" in value:
        out["DisableApiTermination"] = value["disable_api_termination"]
    if "ebs_optimized" in value:
        out["EbsOptimized"] = value["ebs_optimized"]
    if "elastic_gpu_specification_set" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_gpu_specification_set_list

        out["ElasticGpuSpecificationSet"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_gpu_specification_set_list.serialize_json(
                value["elastic_gpu_specification_set"]
            )
        )
    if "elastic_inference_accelerator_set" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_list

        out["ElasticInferenceAcceleratorSet"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_list.serialize_json(
                value["elastic_inference_accelerator_set"]
            )
        )
    if "enclave_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_enclave_options_details

        out["EnclaveOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_enclave_options_details.serialize_json(
                value["enclave_options"]
            )
        )
    if "hibernation_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_hibernation_options_details

        out["HibernationOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_hibernation_options_details.serialize_json(
                value["hibernation_options"]
            )
        )
    if "iam_instance_profile" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_iam_instance_profile_details

        out["IamInstanceProfile"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_iam_instance_profile_details.serialize_json(
                value["iam_instance_profile"]
            )
        )
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "instance_initiated_shutdown_behavior" in value:
        out["InstanceInitiatedShutdownBehavior"] = value[
            "instance_initiated_shutdown_behavior"
        ]
    if "instance_market_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_market_options_details

        out["InstanceMarketOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_market_options_details.serialize_json(
                value["instance_market_options"]
            )
        )
    if "instance_requirements" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_requirements_details

        out["InstanceRequirements"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_requirements_details.serialize_json(
                value["instance_requirements"]
            )
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "kernel_id" in value:
        out["KernelId"] = value["kernel_id"]
    if "key_name" in value:
        out["KeyName"] = value["key_name"]
    if "license_set" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_license_set_list

        out["LicenseSet"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_license_set_list.serialize_json(
                value["license_set"]
            )
        )
    if "maintenance_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_maintenance_options_details

        out["MaintenanceOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_maintenance_options_details.serialize_json(
                value["maintenance_options"]
            )
        )
    if "metadata_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_metadata_options_details

        out["MetadataOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_metadata_options_details.serialize_json(
                value["metadata_options"]
            )
        )
    if "monitoring" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_monitoring_details

        out["Monitoring"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_monitoring_details.serialize_json(
                value["monitoring"]
            )
        )
    if "network_interface_set" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_list

        out["NetworkInterfaceSet"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_list.serialize_json(
                value["network_interface_set"]
            )
        )
    if "placement" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_placement_details

        out["Placement"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_placement_details.serialize_json(
                value["placement"]
            )
        )
    if "private_dns_name_options" in value:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_private_dns_name_options_details

        out["PrivateDnsNameOptions"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_private_dns_name_options_details.serialize_json(
                value["private_dns_name_options"]
            )
        )
    if "ram_disk_id" in value:
        out["RamDiskId"] = value["ram_disk_id"]
    if "security_group_id_set" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["SecurityGroupIdSet"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["security_group_id_set"]
            )
        )
    if "security_group_set" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["SecurityGroupSet"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["security_group_set"]
            )
        )
    if "user_data" in value:
        out["UserData"] = value["user_data"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataDetails:
    out: AwsEc2LaunchTemplateDataDetails = {}  # type: ignore[typeddict-item]
    if "BlockDeviceMappingSet" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_list

        out["block_device_mapping_set"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_block_device_mapping_set_list.deserialize_json(
                data["BlockDeviceMappingSet"]
            )
        )
    if "CapacityReservationSpecification" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_details

        out["capacity_reservation_specification"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_capacity_reservation_specification_details.deserialize_json(
                data["CapacityReservationSpecification"]
            )
        )
    if "CpuOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_cpu_options_details

        out["cpu_options"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_cpu_options_details.deserialize_json(
                data["CpuOptions"]
            )
        )
    if "CreditSpecification" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_credit_specification_details

        out["credit_specification"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_credit_specification_details.deserialize_json(
                data["CreditSpecification"]
            )
        )
    if "DisableApiStop" in data:
        out["disable_api_stop"] = data["DisableApiStop"]
    if "DisableApiTermination" in data:
        out["disable_api_termination"] = data["DisableApiTermination"]
    if "EbsOptimized" in data:
        out["ebs_optimized"] = data["EbsOptimized"]
    if "ElasticGpuSpecificationSet" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_gpu_specification_set_list

        out["elastic_gpu_specification_set"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_gpu_specification_set_list.deserialize_json(
                data["ElasticGpuSpecificationSet"]
            )
        )
    if "ElasticInferenceAcceleratorSet" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_list

        out["elastic_inference_accelerator_set"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_list.deserialize_json(
                data["ElasticInferenceAcceleratorSet"]
            )
        )
    if "EnclaveOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_enclave_options_details

        out["enclave_options"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_enclave_options_details.deserialize_json(
                data["EnclaveOptions"]
            )
        )
    if "HibernationOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_hibernation_options_details

        out["hibernation_options"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_hibernation_options_details.deserialize_json(
                data["HibernationOptions"]
            )
        )
    if "IamInstanceProfile" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_iam_instance_profile_details

        out["iam_instance_profile"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_iam_instance_profile_details.deserialize_json(
                data["IamInstanceProfile"]
            )
        )
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    if "InstanceInitiatedShutdownBehavior" in data:
        out["instance_initiated_shutdown_behavior"] = data[
            "InstanceInitiatedShutdownBehavior"
        ]
    if "InstanceMarketOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_market_options_details

        out["instance_market_options"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_market_options_details.deserialize_json(
                data["InstanceMarketOptions"]
            )
        )
    if "InstanceRequirements" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_requirements_details

        out["instance_requirements"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_instance_requirements_details.deserialize_json(
                data["InstanceRequirements"]
            )
        )
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "KernelId" in data:
        out["kernel_id"] = data["KernelId"]
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    if "LicenseSet" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_license_set_list

        out["license_set"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_license_set_list.deserialize_json(
                data["LicenseSet"]
            )
        )
    if "MaintenanceOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_maintenance_options_details

        out["maintenance_options"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_maintenance_options_details.deserialize_json(
                data["MaintenanceOptions"]
            )
        )
    if "MetadataOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_metadata_options_details

        out["metadata_options"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_metadata_options_details.deserialize_json(
                data["MetadataOptions"]
            )
        )
    if "Monitoring" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_monitoring_details

        out["monitoring"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_monitoring_details.deserialize_json(
                data["Monitoring"]
            )
        )
    if "NetworkInterfaceSet" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_list

        out["network_interface_set"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_network_interface_set_list.deserialize_json(
                data["NetworkInterfaceSet"]
            )
        )
    if "Placement" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_placement_details

        out["placement"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_placement_details.deserialize_json(
                data["Placement"]
            )
        )
    if "PrivateDnsNameOptions" in data:
        import aws_sdk_securityhub.types.aws_ec2_launch_template_data_private_dns_name_options_details

        out["private_dns_name_options"] = (
            aws_sdk_securityhub.types.aws_ec2_launch_template_data_private_dns_name_options_details.deserialize_json(
                data["PrivateDnsNameOptions"]
            )
        )
    if "RamDiskId" in data:
        out["ram_disk_id"] = data["RamDiskId"]
    if "SecurityGroupIdSet" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["security_group_id_set"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["SecurityGroupIdSet"]
            )
        )
    if "SecurityGroupSet" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["security_group_set"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["SecurityGroupSet"]
            )
        )
    if "UserData" in data:
        out["user_data"] = data["UserData"]
    return out
