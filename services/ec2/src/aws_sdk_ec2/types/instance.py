"""Generated from Smithy shape ``com.amazonaws.ec2#Instance``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_values
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boot_mode_values
    import aws_sdk_ec2.types.capacity_reservation_specification_response
    import aws_sdk_ec2.types.cpu_options
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.device_type
    import aws_sdk_ec2.types.elastic_gpu_association_list
    import aws_sdk_ec2.types.elastic_inference_accelerator_association_list
    import aws_sdk_ec2.types.enclave_options
    import aws_sdk_ec2.types.group_identifier_list
    import aws_sdk_ec2.types.hibernation_options
    import aws_sdk_ec2.types.hypervisor_type
    import aws_sdk_ec2.types.iam_instance_profile
    import aws_sdk_ec2.types.instance_block_device_mapping_list
    import aws_sdk_ec2.types.instance_boot_mode_values
    import aws_sdk_ec2.types.instance_lifecycle_type
    import aws_sdk_ec2.types.instance_maintenance_options
    import aws_sdk_ec2.types.instance_metadata_options_response
    import aws_sdk_ec2.types.instance_network_interface_list
    import aws_sdk_ec2.types.instance_network_performance_options
    import aws_sdk_ec2.types.instance_secondary_interface_list
    import aws_sdk_ec2.types.instance_state
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.license_list
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.monitoring
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.placement
    import aws_sdk_ec2.types.platform_values
    import aws_sdk_ec2.types.private_dns_name_options_response
    import aws_sdk_ec2.types.product_code_list
    import aws_sdk_ec2.types.state_reason
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.virtualization_type


class Instance(TypedDict):
    architecture: NotRequired[
        "aws_sdk_ec2.types.architecture_values.ArchitectureValues"
    ]
    """<p>The architecture of the image.</p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.instance_block_device_mapping_list.InstanceBlockDeviceMappingList"
    ]
    """<p>Any block device mapping entries for the instance.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The idempotency token you provided when you launched the instance, if applicable.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.</p>"""
    ena_support: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether enhanced networking with ENA is enabled.</p>"""
    hypervisor: NotRequired["aws_sdk_ec2.types.hypervisor_type.HypervisorType"]
    """<p>The hypervisor type of the instance. The value <code>xen</code> is used for both Xen and Nitro hypervisors.</p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile.IamInstanceProfile"
    ]
    """<p>The IAM instance profile associated with the instance, if applicable.</p>"""
    instance_lifecycle: NotRequired[
        "aws_sdk_ec2.types.instance_lifecycle_type.InstanceLifecycleType"
    ]
    """<p>Indicates whether this is a Spot Instance or a Scheduled Instance.</p>"""
    elastic_gpu_associations: NotRequired[
        "aws_sdk_ec2.types.elastic_gpu_association_list.ElasticGpuAssociationList"
    ]
    """<p>Deprecated.</p> <note> <p>Amazon Elastic Graphics reached end of life on January 8, 2024.</p> </note>"""
    elastic_inference_accelerator_associations: NotRequired[
        "aws_sdk_ec2.types.elastic_inference_accelerator_association_list.ElasticInferenceAcceleratorAssociationList"
    ]
    """<p>Deprecated</p> <note> <p>Amazon Elastic Inference is no longer available.</p> </note>"""
    network_interfaces: NotRequired[
        "aws_sdk_ec2.types.instance_network_interface_list.InstanceNetworkInterfaceList"
    ]
    """<p>The network interfaces for the instance.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    root_device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name of the root device volume (for example, <code>/dev/sda1</code>).</p>"""
    root_device_type: NotRequired["aws_sdk_ec2.types.device_type.DeviceType"]
    """<p>The root device type used by the AMI. The AMI can use an EBS volume or an instance store volume.</p>"""
    security_groups: NotRequired[
        "aws_sdk_ec2.types.group_identifier_list.GroupIdentifierList"
    ]
    """<p>The security groups for the instance.</p>"""
    source_dest_check: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether source/destination checking is enabled.</p>"""
    spot_instance_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If the request is a Spot Instance request, the ID of the request.</p>"""
    sriov_net_support: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.</p>"""
    state_reason: NotRequired["aws_sdk_ec2.types.state_reason.StateReason"]
    """<p>The reason for the most recent state transition.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the instance.</p>"""
    virtualization_type: NotRequired[
        "aws_sdk_ec2.types.virtualization_type.VirtualizationType"
    ]
    """<p>The virtualization type of the instance.</p>"""
    cpu_options: NotRequired["aws_sdk_ec2.types.cpu_options.CpuOptions"]
    """<p>The CPU options for the instance.</p>"""
    capacity_block_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Capacity Block.</p> <note> <p>For P5 instances, a Capacity Block ID refers to a group of instances. For Trn2u instances, a capacity block ID refers to an EC2 UltraServer.</p> </note>"""
    capacity_reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation.</p>"""
    capacity_reservation_specification: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_specification_response.CapacityReservationSpecificationResponse"
    ]
    """<p>Information about the Capacity Reservation targeting option.</p>"""
    hibernation_options: NotRequired[
        "aws_sdk_ec2.types.hibernation_options.HibernationOptions"
    ]
    """<p>Indicates whether the instance is enabled for hibernation.</p>"""
    licenses: NotRequired["aws_sdk_ec2.types.license_list.LicenseList"]
    """<p>The license configurations for the instance.</p>"""
    metadata_options: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_options_response.InstanceMetadataOptionsResponse"
    ]
    """<p>The metadata options for the instance.</p>"""
    enclave_options: NotRequired["aws_sdk_ec2.types.enclave_options.EnclaveOptions"]
    """<p>Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.</p>"""
    boot_mode: NotRequired["aws_sdk_ec2.types.boot_mode_values.BootModeValues"]
    """<p>The boot mode that was specified by the AMI. If the value is <code>uefi-preferred</code>, the AMI supports both UEFI and Legacy BIOS. The <code>currentInstanceBootMode</code> parameter is the boot mode that is used to boot the instance at launch or start.</p> <note> <p>The operating system contained in the AMI must be configured to support the specified boot mode.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html\">Boot modes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    platform_details: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The platform details value for the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html\">AMI billing information fields</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    usage_operation: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The usage operation value for the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html\">AMI billing information fields</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    usage_operation_update_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time that the usage operation was last updated.</p>"""
    private_dns_name_options: NotRequired[
        "aws_sdk_ec2.types.private_dns_name_options_response.PrivateDnsNameOptionsResponse"
    ]
    """<p>The options for the instance hostname.</p>"""
    ipv6_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 address assigned to the instance.</p>"""
    tpm_support: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If the instance is configured for NitroTPM support, the value is <code>v2.0</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html\">NitroTPM</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    maintenance_options: NotRequired[
        "aws_sdk_ec2.types.instance_maintenance_options.InstanceMaintenanceOptions"
    ]
    """<p>Provides information on the recovery and maintenance options of your instance.</p>"""
    current_instance_boot_mode: NotRequired[
        "aws_sdk_ec2.types.instance_boot_mode_values.InstanceBootModeValues"
    ]
    """<p>The boot mode that is used to boot the instance at launch or start. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html\">Boot modes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    network_performance_options: NotRequired[
        "aws_sdk_ec2.types.instance_network_performance_options.InstanceNetworkPerformanceOptions"
    ]
    """<p>Contains settings for the network performance options for your instance.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the instance.</p>"""
    secondary_interfaces: NotRequired[
        "aws_sdk_ec2.types.instance_secondary_interface_list.InstanceSecondaryInterfaceList"
    ]
    """<p>The secondary interfaces for the instance.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the AMI used to launch the instance.</p>"""
    state: NotRequired["aws_sdk_ec2.types.instance_state.InstanceState"]
    """<p>The current state of the instance.</p>"""
    private_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>[IPv4 only] The private DNS hostname name assigned to the instance. This DNS hostname can only be used inside the Amazon EC2 network. This name is not available until the instance enters the <code>running</code> state. </p> <p>The Amazon-provided DNS server resolves Amazon-provided private DNS hostnames if you've enabled DNS resolution and DNS hostnames in your VPC. If you are not using the Amazon-provided DNS server in your VPC, your custom domain name servers must resolve the hostname as appropriate.</p>"""
    public_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public DNS name assigned to the instance. This name is not available until the instance enters the <code>running</code> state. This name is only available if you've enabled DNS hostnames for your VPC. The format of this name depends on the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hostname-types.html#public-hostnames\">public hostname type</a>.</p>"""
    state_transition_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the most recent state transition. This might be an empty string.</p>"""
    key_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the key pair, if this instance was launched with an associated key pair.</p>"""
    ami_launch_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The AMI launch index, which can be used to find this instance in the launch group.</p>"""
    product_codes: NotRequired["aws_sdk_ec2.types.product_code_list.ProductCodeList"]
    """<p>The product codes attached to this instance, if applicable.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    launch_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time that the instance was last launched. To determine the time that instance was first launched, see the attachment time for the primary network interface.</p>"""
    placement: NotRequired["aws_sdk_ec2.types.placement.Placement"]
    """<p>The location where the instance launched, if applicable.</p>"""
    kernel_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The kernel associated with this instance, if applicable.</p>"""
    ramdisk_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The RAM disk associated with this instance, if applicable.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.platform_values.PlatformValues"]
    """<p>The platform. This value is <code>windows</code> for Windows instances; otherwise, it is empty.</p>"""
    monitoring: NotRequired["aws_sdk_ec2.types.monitoring.Monitoring"]
    """<p>The monitoring for the instance.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet in which the instance is running.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC in which the instance is running.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private IPv4 address assigned to the instance.</p>"""
    public_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The public IPv4 address, or the Carrier IP address assigned to the instance, if applicable.</p> <p>A Carrier IP address only applies to an instance launched in a subnet associated with a Wavelength Zone.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Instance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "architecture" in value:
        import aws_sdk_ec2.types.architecture_values

        aws_sdk_ec2.types.architecture_values.serialize_ec2_query(
            value["architecture"], pairs, f"{prefix}.Architecture"
        )
    if "block_device_mappings" in value:
        import aws_sdk_ec2.types.instance_block_device_mapping_list

        aws_sdk_ec2.types.instance_block_device_mapping_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{prefix}.BlockDeviceMapping"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "ebs_optimized" in value:
        pairs.append(
            (f"{prefix}.EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "ena_support" in value:
        pairs.append(
            (f"{prefix}.EnaSupport", "true" if value["ena_support"] else "false")
        )
    if "hypervisor" in value:
        import aws_sdk_ec2.types.hypervisor_type

        aws_sdk_ec2.types.hypervisor_type.serialize_ec2_query(
            value["hypervisor"], pairs, f"{prefix}.Hypervisor"
        )
    if "iam_instance_profile" in value:
        import aws_sdk_ec2.types.iam_instance_profile

        aws_sdk_ec2.types.iam_instance_profile.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{prefix}.IamInstanceProfile"
        )
    if "instance_lifecycle" in value:
        import aws_sdk_ec2.types.instance_lifecycle_type

        aws_sdk_ec2.types.instance_lifecycle_type.serialize_ec2_query(
            value["instance_lifecycle"], pairs, f"{prefix}.InstanceLifecycle"
        )
    if "elastic_gpu_associations" in value:
        import aws_sdk_ec2.types.elastic_gpu_association_list

        aws_sdk_ec2.types.elastic_gpu_association_list.serialize_ec2_query(
            value["elastic_gpu_associations"],
            pairs,
            f"{prefix}.ElasticGpuAssociationSet",
        )
    if "elastic_inference_accelerator_associations" in value:
        import aws_sdk_ec2.types.elastic_inference_accelerator_association_list

        aws_sdk_ec2.types.elastic_inference_accelerator_association_list.serialize_ec2_query(
            value["elastic_inference_accelerator_associations"],
            pairs,
            f"{prefix}.ElasticInferenceAcceleratorAssociationSet",
        )
    if "network_interfaces" in value:
        import aws_sdk_ec2.types.instance_network_interface_list

        aws_sdk_ec2.types.instance_network_interface_list.serialize_ec2_query(
            value["network_interfaces"], pairs, f"{prefix}.NetworkInterfaceSet"
        )
    if "outpost_arn" in value:
        pairs.append((f"{prefix}.OutpostArn", str(value["outpost_arn"])))
    if "root_device_name" in value:
        pairs.append((f"{prefix}.RootDeviceName", str(value["root_device_name"])))
    if "root_device_type" in value:
        import aws_sdk_ec2.types.device_type

        aws_sdk_ec2.types.device_type.serialize_ec2_query(
            value["root_device_type"], pairs, f"{prefix}.RootDeviceType"
        )
    if "security_groups" in value:
        import aws_sdk_ec2.types.group_identifier_list

        aws_sdk_ec2.types.group_identifier_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{prefix}.GroupSet"
        )
    if "source_dest_check" in value:
        pairs.append(
            (
                f"{prefix}.SourceDestCheck",
                "true" if value["source_dest_check"] else "false",
            )
        )
    if "spot_instance_request_id" in value:
        pairs.append(
            (f"{prefix}.SpotInstanceRequestId", str(value["spot_instance_request_id"]))
        )
    if "sriov_net_support" in value:
        pairs.append((f"{prefix}.SriovNetSupport", str(value["sriov_net_support"])))
    if "state_reason" in value:
        import aws_sdk_ec2.types.state_reason

        aws_sdk_ec2.types.state_reason.serialize_ec2_query(
            value["state_reason"], pairs, f"{prefix}.StateReason"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "virtualization_type" in value:
        import aws_sdk_ec2.types.virtualization_type

        aws_sdk_ec2.types.virtualization_type.serialize_ec2_query(
            value["virtualization_type"], pairs, f"{prefix}.VirtualizationType"
        )
    if "cpu_options" in value:
        import aws_sdk_ec2.types.cpu_options

        aws_sdk_ec2.types.cpu_options.serialize_ec2_query(
            value["cpu_options"], pairs, f"{prefix}.CpuOptions"
        )
    if "capacity_block_id" in value:
        pairs.append((f"{prefix}.CapacityBlockId", str(value["capacity_block_id"])))
    if "capacity_reservation_id" in value:
        pairs.append(
            (f"{prefix}.CapacityReservationId", str(value["capacity_reservation_id"]))
        )
    if "capacity_reservation_specification" in value:
        import aws_sdk_ec2.types.capacity_reservation_specification_response

        aws_sdk_ec2.types.capacity_reservation_specification_response.serialize_ec2_query(
            value["capacity_reservation_specification"],
            pairs,
            f"{prefix}.CapacityReservationSpecification",
        )
    if "hibernation_options" in value:
        import aws_sdk_ec2.types.hibernation_options

        aws_sdk_ec2.types.hibernation_options.serialize_ec2_query(
            value["hibernation_options"], pairs, f"{prefix}.HibernationOptions"
        )
    if "licenses" in value:
        import aws_sdk_ec2.types.license_list

        aws_sdk_ec2.types.license_list.serialize_ec2_query(
            value["licenses"], pairs, f"{prefix}.LicenseSet"
        )
    if "metadata_options" in value:
        import aws_sdk_ec2.types.instance_metadata_options_response

        aws_sdk_ec2.types.instance_metadata_options_response.serialize_ec2_query(
            value["metadata_options"], pairs, f"{prefix}.MetadataOptions"
        )
    if "enclave_options" in value:
        import aws_sdk_ec2.types.enclave_options

        aws_sdk_ec2.types.enclave_options.serialize_ec2_query(
            value["enclave_options"], pairs, f"{prefix}.EnclaveOptions"
        )
    if "boot_mode" in value:
        import aws_sdk_ec2.types.boot_mode_values

        aws_sdk_ec2.types.boot_mode_values.serialize_ec2_query(
            value["boot_mode"], pairs, f"{prefix}.BootMode"
        )
    if "platform_details" in value:
        pairs.append((f"{prefix}.PlatformDetails", str(value["platform_details"])))
    if "usage_operation" in value:
        pairs.append((f"{prefix}.UsageOperation", str(value["usage_operation"])))
    if "usage_operation_update_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["usage_operation_update_time"],
            pairs,
            f"{prefix}.UsageOperationUpdateTime",
        )
    if "private_dns_name_options" in value:
        import aws_sdk_ec2.types.private_dns_name_options_response

        aws_sdk_ec2.types.private_dns_name_options_response.serialize_ec2_query(
            value["private_dns_name_options"], pairs, f"{prefix}.PrivateDnsNameOptions"
        )
    if "ipv6_address" in value:
        pairs.append((f"{prefix}.Ipv6Address", str(value["ipv6_address"])))
    if "tpm_support" in value:
        pairs.append((f"{prefix}.TpmSupport", str(value["tpm_support"])))
    if "maintenance_options" in value:
        import aws_sdk_ec2.types.instance_maintenance_options

        aws_sdk_ec2.types.instance_maintenance_options.serialize_ec2_query(
            value["maintenance_options"], pairs, f"{prefix}.MaintenanceOptions"
        )
    if "current_instance_boot_mode" in value:
        import aws_sdk_ec2.types.instance_boot_mode_values

        aws_sdk_ec2.types.instance_boot_mode_values.serialize_ec2_query(
            value["current_instance_boot_mode"],
            pairs,
            f"{prefix}.CurrentInstanceBootMode",
        )
    if "network_performance_options" in value:
        import aws_sdk_ec2.types.instance_network_performance_options

        aws_sdk_ec2.types.instance_network_performance_options.serialize_ec2_query(
            value["network_performance_options"],
            pairs,
            f"{prefix}.NetworkPerformanceOptions",
        )
    if "operator" in value:
        import aws_sdk_ec2.types.operator_response

        aws_sdk_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{prefix}.Operator"
        )
    if "secondary_interfaces" in value:
        import aws_sdk_ec2.types.instance_secondary_interface_list

        aws_sdk_ec2.types.instance_secondary_interface_list.serialize_ec2_query(
            value["secondary_interfaces"], pairs, f"{prefix}.SecondaryInterfaceSet"
        )
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.instance_state

        aws_sdk_ec2.types.instance_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.InstanceState"
        )
    if "private_dns_name" in value:
        pairs.append((f"{prefix}.PrivateDnsName", str(value["private_dns_name"])))
    if "public_dns_name" in value:
        pairs.append((f"{prefix}.DnsName", str(value["public_dns_name"])))
    if "state_transition_reason" in value:
        pairs.append((f"{prefix}.Reason", str(value["state_transition_reason"])))
    if "key_name" in value:
        pairs.append((f"{prefix}.KeyName", str(value["key_name"])))
    if "ami_launch_index" in value:
        pairs.append((f"{prefix}.AmiLaunchIndex", str(value["ami_launch_index"])))
    if "product_codes" in value:
        import aws_sdk_ec2.types.product_code_list

        aws_sdk_ec2.types.product_code_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{prefix}.ProductCodes"
        )
    if "instance_type" in value:
        import aws_sdk_ec2.types.instance_type

        aws_sdk_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{prefix}.InstanceType"
        )
    if "launch_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["launch_time"], pairs, f"{prefix}.LaunchTime"
        )
    if "placement" in value:
        import aws_sdk_ec2.types.placement

        aws_sdk_ec2.types.placement.serialize_ec2_query(
            value["placement"], pairs, f"{prefix}.Placement"
        )
    if "kernel_id" in value:
        pairs.append((f"{prefix}.KernelId", str(value["kernel_id"])))
    if "ramdisk_id" in value:
        pairs.append((f"{prefix}.RamdiskId", str(value["ramdisk_id"])))
    if "platform" in value:
        import aws_sdk_ec2.types.platform_values

        aws_sdk_ec2.types.platform_values.serialize_ec2_query(
            value["platform"], pairs, f"{prefix}.Platform"
        )
    if "monitoring" in value:
        import aws_sdk_ec2.types.monitoring

        aws_sdk_ec2.types.monitoring.serialize_ec2_query(
            value["monitoring"], pairs, f"{prefix}.Monitoring"
        )
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "private_ip_address" in value:
        pairs.append((f"{prefix}.PrivateIpAddress", str(value["private_ip_address"])))
    if "public_ip_address" in value:
        pairs.append((f"{prefix}.IpAddress", str(value["public_ip_address"])))


def deserialize_ec2_query(el: Element) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    child_architecture = el.find("Architecture")
    if child_architecture is not None:
        import aws_sdk_ec2.types.architecture_values

        out["architecture"] = (
            aws_sdk_ec2.types.architecture_values.deserialize_ec2_query(
                child_architecture
            )
        )
    if el.find("BlockDeviceMapping") is not None:
        import aws_sdk_ec2.types.instance_block_device_mapping_list

        out["block_device_mappings"] = (
            aws_sdk_ec2.types.instance_block_device_mapping_list.deserialize_ec2_query(
                el, "BlockDeviceMapping"
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_ebs_optimized = el.find("EbsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_ena_support = el.find("EnaSupport")
    if child_ena_support is not None:
        out["ena_support"] = (child_ena_support.text or "").lower() == "true"
    child_hypervisor = el.find("Hypervisor")
    if child_hypervisor is not None:
        import aws_sdk_ec2.types.hypervisor_type

        out["hypervisor"] = aws_sdk_ec2.types.hypervisor_type.deserialize_ec2_query(
            child_hypervisor
        )
    child_iam_instance_profile = el.find("IamInstanceProfile")
    if child_iam_instance_profile is not None:
        import aws_sdk_ec2.types.iam_instance_profile

        out["iam_instance_profile"] = (
            aws_sdk_ec2.types.iam_instance_profile.deserialize_ec2_query(
                child_iam_instance_profile
            )
        )
    child_instance_lifecycle = el.find("InstanceLifecycle")
    if child_instance_lifecycle is not None:
        import aws_sdk_ec2.types.instance_lifecycle_type

        out["instance_lifecycle"] = (
            aws_sdk_ec2.types.instance_lifecycle_type.deserialize_ec2_query(
                child_instance_lifecycle
            )
        )
    if el.find("ElasticGpuAssociationSet") is not None:
        import aws_sdk_ec2.types.elastic_gpu_association_list

        out["elastic_gpu_associations"] = (
            aws_sdk_ec2.types.elastic_gpu_association_list.deserialize_ec2_query(
                el, "ElasticGpuAssociationSet"
            )
        )
    if el.find("ElasticInferenceAcceleratorAssociationSet") is not None:
        import aws_sdk_ec2.types.elastic_inference_accelerator_association_list

        out["elastic_inference_accelerator_associations"] = (
            aws_sdk_ec2.types.elastic_inference_accelerator_association_list.deserialize_ec2_query(
                el, "ElasticInferenceAcceleratorAssociationSet"
            )
        )
    if el.find("NetworkInterfaceSet") is not None:
        import aws_sdk_ec2.types.instance_network_interface_list

        out["network_interfaces"] = (
            aws_sdk_ec2.types.instance_network_interface_list.deserialize_ec2_query(
                el, "NetworkInterfaceSet"
            )
        )
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_root_device_name = el.find("RootDeviceName")
    if child_root_device_name is not None:
        out["root_device_name"] = str(child_root_device_name.text or "")
    child_root_device_type = el.find("RootDeviceType")
    if child_root_device_type is not None:
        import aws_sdk_ec2.types.device_type

        out["root_device_type"] = aws_sdk_ec2.types.device_type.deserialize_ec2_query(
            child_root_device_type
        )
    if el.find("GroupSet") is not None:
        import aws_sdk_ec2.types.group_identifier_list

        out["security_groups"] = (
            aws_sdk_ec2.types.group_identifier_list.deserialize_ec2_query(
                el, "GroupSet"
            )
        )
    child_source_dest_check = el.find("SourceDestCheck")
    if child_source_dest_check is not None:
        out["source_dest_check"] = (
            child_source_dest_check.text or ""
        ).lower() == "true"
    child_spot_instance_request_id = el.find("SpotInstanceRequestId")
    if child_spot_instance_request_id is not None:
        out["spot_instance_request_id"] = str(child_spot_instance_request_id.text or "")
    child_sriov_net_support = el.find("SriovNetSupport")
    if child_sriov_net_support is not None:
        out["sriov_net_support"] = str(child_sriov_net_support.text or "")
    child_state_reason = el.find("StateReason")
    if child_state_reason is not None:
        import aws_sdk_ec2.types.state_reason

        out["state_reason"] = aws_sdk_ec2.types.state_reason.deserialize_ec2_query(
            child_state_reason
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_virtualization_type = el.find("VirtualizationType")
    if child_virtualization_type is not None:
        import aws_sdk_ec2.types.virtualization_type

        out["virtualization_type"] = (
            aws_sdk_ec2.types.virtualization_type.deserialize_ec2_query(
                child_virtualization_type
            )
        )
    child_cpu_options = el.find("CpuOptions")
    if child_cpu_options is not None:
        import aws_sdk_ec2.types.cpu_options

        out["cpu_options"] = aws_sdk_ec2.types.cpu_options.deserialize_ec2_query(
            child_cpu_options
        )
    child_capacity_block_id = el.find("CapacityBlockId")
    if child_capacity_block_id is not None:
        out["capacity_block_id"] = str(child_capacity_block_id.text or "")
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_capacity_reservation_specification = el.find(
        "CapacityReservationSpecification"
    )
    if child_capacity_reservation_specification is not None:
        import aws_sdk_ec2.types.capacity_reservation_specification_response

        out["capacity_reservation_specification"] = (
            aws_sdk_ec2.types.capacity_reservation_specification_response.deserialize_ec2_query(
                child_capacity_reservation_specification
            )
        )
    child_hibernation_options = el.find("HibernationOptions")
    if child_hibernation_options is not None:
        import aws_sdk_ec2.types.hibernation_options

        out["hibernation_options"] = (
            aws_sdk_ec2.types.hibernation_options.deserialize_ec2_query(
                child_hibernation_options
            )
        )
    if el.find("LicenseSet") is not None:
        import aws_sdk_ec2.types.license_list

        out["licenses"] = aws_sdk_ec2.types.license_list.deserialize_ec2_query(
            el, "LicenseSet"
        )
    child_metadata_options = el.find("MetadataOptions")
    if child_metadata_options is not None:
        import aws_sdk_ec2.types.instance_metadata_options_response

        out["metadata_options"] = (
            aws_sdk_ec2.types.instance_metadata_options_response.deserialize_ec2_query(
                child_metadata_options
            )
        )
    child_enclave_options = el.find("EnclaveOptions")
    if child_enclave_options is not None:
        import aws_sdk_ec2.types.enclave_options

        out["enclave_options"] = (
            aws_sdk_ec2.types.enclave_options.deserialize_ec2_query(
                child_enclave_options
            )
        )
    child_boot_mode = el.find("BootMode")
    if child_boot_mode is not None:
        import aws_sdk_ec2.types.boot_mode_values

        out["boot_mode"] = aws_sdk_ec2.types.boot_mode_values.deserialize_ec2_query(
            child_boot_mode
        )
    child_platform_details = el.find("PlatformDetails")
    if child_platform_details is not None:
        out["platform_details"] = str(child_platform_details.text or "")
    child_usage_operation = el.find("UsageOperation")
    if child_usage_operation is not None:
        out["usage_operation"] = str(child_usage_operation.text or "")
    child_usage_operation_update_time = el.find("UsageOperationUpdateTime")
    if child_usage_operation_update_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["usage_operation_update_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_usage_operation_update_time
            )
        )
    child_private_dns_name_options = el.find("PrivateDnsNameOptions")
    if child_private_dns_name_options is not None:
        import aws_sdk_ec2.types.private_dns_name_options_response

        out["private_dns_name_options"] = (
            aws_sdk_ec2.types.private_dns_name_options_response.deserialize_ec2_query(
                child_private_dns_name_options
            )
        )
    child_ipv6_address = el.find("Ipv6Address")
    if child_ipv6_address is not None:
        out["ipv6_address"] = str(child_ipv6_address.text or "")
    child_tpm_support = el.find("TpmSupport")
    if child_tpm_support is not None:
        out["tpm_support"] = str(child_tpm_support.text or "")
    child_maintenance_options = el.find("MaintenanceOptions")
    if child_maintenance_options is not None:
        import aws_sdk_ec2.types.instance_maintenance_options

        out["maintenance_options"] = (
            aws_sdk_ec2.types.instance_maintenance_options.deserialize_ec2_query(
                child_maintenance_options
            )
        )
    child_current_instance_boot_mode = el.find("CurrentInstanceBootMode")
    if child_current_instance_boot_mode is not None:
        import aws_sdk_ec2.types.instance_boot_mode_values

        out["current_instance_boot_mode"] = (
            aws_sdk_ec2.types.instance_boot_mode_values.deserialize_ec2_query(
                child_current_instance_boot_mode
            )
        )
    child_network_performance_options = el.find("NetworkPerformanceOptions")
    if child_network_performance_options is not None:
        import aws_sdk_ec2.types.instance_network_performance_options

        out["network_performance_options"] = (
            aws_sdk_ec2.types.instance_network_performance_options.deserialize_ec2_query(
                child_network_performance_options
            )
        )
    child_operator = el.find("Operator")
    if child_operator is not None:
        import aws_sdk_ec2.types.operator_response

        out["operator"] = aws_sdk_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    if el.find("SecondaryInterfaceSet") is not None:
        import aws_sdk_ec2.types.instance_secondary_interface_list

        out["secondary_interfaces"] = (
            aws_sdk_ec2.types.instance_secondary_interface_list.deserialize_ec2_query(
                el, "SecondaryInterfaceSet"
            )
        )
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_state = el.find("InstanceState")
    if child_state is not None:
        import aws_sdk_ec2.types.instance_state

        out["state"] = aws_sdk_ec2.types.instance_state.deserialize_ec2_query(
            child_state
        )
    child_private_dns_name = el.find("PrivateDnsName")
    if child_private_dns_name is not None:
        out["private_dns_name"] = str(child_private_dns_name.text or "")
    child_public_dns_name = el.find("DnsName")
    if child_public_dns_name is not None:
        out["public_dns_name"] = str(child_public_dns_name.text or "")
    child_state_transition_reason = el.find("Reason")
    if child_state_transition_reason is not None:
        out["state_transition_reason"] = str(child_state_transition_reason.text or "")
    child_key_name = el.find("KeyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_ami_launch_index = el.find("AmiLaunchIndex")
    if child_ami_launch_index is not None:
        out["ami_launch_index"] = int(child_ami_launch_index.text or "")
    if el.find("ProductCodes") is not None:
        import aws_sdk_ec2.types.product_code_list

        out["product_codes"] = (
            aws_sdk_ec2.types.product_code_list.deserialize_ec2_query(
                el, "ProductCodes"
            )
        )
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import aws_sdk_ec2.types.instance_type

        out["instance_type"] = aws_sdk_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_launch_time = el.find("LaunchTime")
    if child_launch_time is not None:
        import aws_sdk_ec2.types.date_time

        out["launch_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_launch_time
        )
    child_placement = el.find("Placement")
    if child_placement is not None:
        import aws_sdk_ec2.types.placement

        out["placement"] = aws_sdk_ec2.types.placement.deserialize_ec2_query(
            child_placement
        )
    child_kernel_id = el.find("KernelId")
    if child_kernel_id is not None:
        out["kernel_id"] = str(child_kernel_id.text or "")
    child_ramdisk_id = el.find("RamdiskId")
    if child_ramdisk_id is not None:
        out["ramdisk_id"] = str(child_ramdisk_id.text or "")
    child_platform = el.find("Platform")
    if child_platform is not None:
        import aws_sdk_ec2.types.platform_values

        out["platform"] = aws_sdk_ec2.types.platform_values.deserialize_ec2_query(
            child_platform
        )
    child_monitoring = el.find("Monitoring")
    if child_monitoring is not None:
        import aws_sdk_ec2.types.monitoring

        out["monitoring"] = aws_sdk_ec2.types.monitoring.deserialize_ec2_query(
            child_monitoring
        )
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    child_public_ip_address = el.find("IpAddress")
    if child_public_ip_address is not None:
        out["public_ip_address"] = str(child_public_ip_address.text or "")
    return out
