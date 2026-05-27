"""Generated from Smithy shape ``com.amazonaws.ec2#Instance``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
