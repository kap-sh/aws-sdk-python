"""Generated from Smithy shape ``com.amazonaws.ec2#RunInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.block_device_mapping_request_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_specification
    import aws_sdk_ec2.types.cpu_options_request
    import aws_sdk_ec2.types.credit_specification_request
    import aws_sdk_ec2.types.elastic_gpu_specifications
    import aws_sdk_ec2.types.elastic_inference_accelerators
    import aws_sdk_ec2.types.enclave_options_request
    import aws_sdk_ec2.types.hibernation_options_request
    import aws_sdk_ec2.types.iam_instance_profile_specification
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.instance_ipv6_address_list
    import aws_sdk_ec2.types.instance_maintenance_options_request
    import aws_sdk_ec2.types.instance_market_options_request
    import aws_sdk_ec2.types.instance_metadata_options_request
    import aws_sdk_ec2.types.instance_network_interface_specification_list
    import aws_sdk_ec2.types.instance_network_performance_options_request
    import aws_sdk_ec2.types.instance_secondary_interface_specification_list_request
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.kernel_id
    import aws_sdk_ec2.types.key_pair_name
    import aws_sdk_ec2.types.launch_template_specification
    import aws_sdk_ec2.types.license_specification_list_request
    import aws_sdk_ec2.types.operator_request
    import aws_sdk_ec2.types.placement
    import aws_sdk_ec2.types.private_dns_name_options_request
    import aws_sdk_ec2.types.ramdisk_id
    import aws_sdk_ec2.types.run_instances_monitoring_enabled
    import aws_sdk_ec2.types.run_instances_user_data
    import aws_sdk_ec2.types.security_group_id_string_list
    import aws_sdk_ec2.types.security_group_string_list
    import aws_sdk_ec2.types.shutdown_behavior
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_specification_list


class RunInstancesRequest(TypedDict):
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.block_device_mapping_request_list.BlockDeviceMappingRequestList"
    ]
    """<p>The block device mapping, which defines the EBS volumes and instance store volumes to attach to the instance at launch. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html\">Block device mappings</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI. An AMI ID is required to launch an instance and must be specified here or in a launch template.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html\">Amazon EC2 Instance Types Guide</a>.</p>"""
    ipv6_address_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.</p> <p>You cannot specify this option and the network interfaces option in the same request.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.instance_ipv6_address_list.InstanceIpv6AddressList"
    ]
    """<p>The IPv6 addresses from the range of the subnet to associate with the primary network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.</p> <p>You cannot specify this option and the network interfaces option in the same request.</p>"""
    kernel_id: NotRequired["aws_sdk_ec2.types.kernel_id.KernelId"]
    """<p>The ID of the kernel.</p> <important> <p>We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html\">PV-GRUB</a> in the <i>Amazon EC2 User Guide</i>.</p> </important>"""
    key_name: NotRequired["aws_sdk_ec2.types.key_pair_name.KeyPairName"]
    """<p>The name of the key pair. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html\">Create a key pair for your EC2 instance</a>.</p> <important> <p>If you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.</p> </important>"""
    max_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of instances to launch. If you specify a value that is more capacity than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches the largest possible number of instances above the specified minimum count.</p> <p>Constraints: Between 1 and the quota for the specified instance type for your account for this Region. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-quotas.html\">Amazon EC2 instance type quotas</a>.</p>"""
    min_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum number of instances to launch. If you specify a value that is more capacity than Amazon EC2 can provide in the target Availability Zone, Amazon EC2 does not launch any instances.</p> <p>Constraints: Between 1 and the quota for the specified instance type for your account for this Region. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-quotas.html\">Amazon EC2 instance type quotas</a>.</p>"""
    monitoring: NotRequired[
        "aws_sdk_ec2.types.run_instances_monitoring_enabled.RunInstancesMonitoringEnabled"
    ]
    """<p>Specifies whether detailed monitoring is enabled for the instance.</p>"""
    placement: NotRequired["aws_sdk_ec2.types.placement.Placement"]
    """<p>The placement for the instance.</p>"""
    ramdisk_id: NotRequired["aws_sdk_ec2.types.ramdisk_id.RamdiskId"]
    """<p>The ID of the RAM disk to select. Some kernels require additional drivers at launch. Check the kernel requirements for information about whether you need to specify a RAM disk. To find kernel requirements, go to the Amazon Web Services Resource Center and search for the kernel ID.</p> <important> <p>We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html\">PV-GRUB</a> in the <i>Amazon EC2 User Guide</i>.</p> </important>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>The IDs of the security groups.</p> <p>If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.</p>"""
    security_groups: NotRequired[
        "aws_sdk_ec2.types.security_group_string_list.SecurityGroupStringList"
    ]
    """<p>[Default VPC] The names of the security groups.</p> <p>If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.</p> <p>Default: Amazon EC2 uses the default security group.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet to launch the instance into.</p> <p>If you specify a network interface, you must specify any subnets as part of the network interface instead of using this parameter.</p>"""
    user_data: NotRequired[
        "aws_sdk_ec2.types.run_instances_user_data.RunInstancesUserData"
    ]
    """<p>The user data to make available to the instance. User data must be base64-encoded. Depending on the tool or SDK that you're using, the base64-encoding might be performed for you. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html\">Run commands at launch using instance user data</a>.</p>"""
    elastic_gpu_specification: NotRequired[
        "aws_sdk_ec2.types.elastic_gpu_specifications.ElasticGpuSpecifications"
    ]
    """<p>An elastic GPU to associate with the instance.</p> <note> <p>Amazon Elastic Graphics reached end of life on January 8, 2024.</p> </note>"""
    elastic_inference_accelerators: NotRequired[
        "aws_sdk_ec2.types.elastic_inference_accelerators.ElasticInferenceAccelerators"
    ]
    """<p>An elastic inference accelerator to associate with the instance.</p> <note> <p>Amazon Elastic Inference is no longer available.</p> </note>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the resources that are created during instance launch.</p> <p>You can specify tags for the following resources only:</p> <ul> <li> <p>Instances</p> </li> <li> <p>Volumes</p> </li> <li> <p>Spot Instance requests</p> </li> <li> <p>Network interfaces</p> </li> </ul> <p>To tag a resource after it has been created, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html\">CreateTags</a>.</p>"""
    launch_template: NotRequired[
        "aws_sdk_ec2.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>The launch template. Any additional parameters that you specify for the new instance overwrite the corresponding parameters included in the launch template.</p>"""
    instance_market_options: NotRequired[
        "aws_sdk_ec2.types.instance_market_options_request.InstanceMarketOptionsRequest"
    ]
    """<p>The market (purchasing) option for the instances.</p> <p>For <a>RunInstances</a>, persistent Spot Instance requests are only supported when <b>InstanceInterruptionBehavior</b> is set to either <code>hibernate</code> or <code>stop</code>.</p>"""
    credit_specification: NotRequired[
        "aws_sdk_ec2.types.credit_specification_request.CreditSpecificationRequest"
    ]
    """<p>The credit option for CPU usage of the burstable performance instance. Valid values are <code>standard</code> and <code>unlimited</code>. To change this attribute after launch, use <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCreditSpecification.html\"> ModifyInstanceCreditSpecification</a>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html\">Burstable performance instances</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>standard</code> (T2 instances) or <code>unlimited</code> (T3/T3a/T4g instances)</p> <p>For T3 instances with <code>host</code> tenancy, only <code>standard</code> is supported.</p>"""
    cpu_options: NotRequired["aws_sdk_ec2.types.cpu_options_request.CpuOptionsRequest"]
    """<p>The CPU options for the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html\">Optimize CPU options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    capacity_reservation_specification: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_specification.CapacityReservationSpecification"
    ]
    """<p>Information about the Capacity Reservation targeting option. If you do not specify this parameter, the instance's Capacity Reservation preference defaults to <code>open</code>, which enables it to run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone, and tenancy).</p>"""
    hibernation_options: NotRequired[
        "aws_sdk_ec2.types.hibernation_options_request.HibernationOptionsRequest"
    ]
    """<p>Indicates whether an instance is enabled for hibernation. This parameter is valid only if the instance meets the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html\">hibernation prerequisites</a>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html\">Hibernate your Amazon EC2 instance</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>You can't enable hibernation and Amazon Web Services Nitro Enclaves on the same instance.</p>"""
    license_specifications: NotRequired[
        "aws_sdk_ec2.types.license_specification_list_request.LicenseSpecificationListRequest"
    ]
    """<p>The license configurations.</p>"""
    metadata_options: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_options_request.InstanceMetadataOptionsRequest"
    ]
    """<p>The metadata options for the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html\">Configure the Instance Metadata Service options</a>.</p>"""
    enclave_options: NotRequired[
        "aws_sdk_ec2.types.enclave_options_request.EnclaveOptionsRequest"
    ]
    """<p>Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves. For more information, see <a href=\"https://docs.aws.amazon.com/enclaves/latest/user/\">Amazon Web Services Nitro Enclaves User Guide</a>.</p> <p>You can't enable Amazon Web Services Nitro Enclaves and hibernation on the same instance.</p>"""
    private_dns_name_options: NotRequired[
        "aws_sdk_ec2.types.private_dns_name_options_request.PrivateDnsNameOptionsRequest"
    ]
    """<p>The options for the instance hostname. The default values are inherited from the subnet. Applies only if creating a network interface, not attaching an existing one.</p>"""
    maintenance_options: NotRequired[
        "aws_sdk_ec2.types.instance_maintenance_options_request.InstanceMaintenanceOptionsRequest"
    ]
    """<p>The maintenance and recovery options for the instance.</p>"""
    disable_api_stop: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether an instance is enabled for stop protection. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html\">Enable stop protection for your EC2 instances</a>.</p>"""
    enable_primary_ipv6: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If you’re launching an instance into a dual-stack or IPv6-only subnet, you can enable assigning a primary IPv6 address. A primary IPv6 address is an IPv6 GUA address associated with an ENI that you have enabled to use a primary IPv6 address. Use this option if an instance relies on its IPv6 address not changing. When you launch the instance, Amazon Web Services will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. Once you enable an IPv6 GUA address to be a primary IPv6, you cannot disable it. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.</p>"""
    network_performance_options: NotRequired[
        "aws_sdk_ec2.types.instance_network_performance_options_request.InstanceNetworkPerformanceOptionsRequest"
    ]
    """<p>Contains settings for the network performance options for the instance.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_request.OperatorRequest"]
    """<p>Reserved for internal use.</p>"""
    secondary_interfaces: NotRequired[
        "aws_sdk_ec2.types.instance_secondary_interface_specification_list_request.InstanceSecondaryInterfaceSpecificationListRequest"
    ]
    """<p>The secondary interfaces to associate with the instance.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    disable_api_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether termination protection is enabled for the instance. The default is <code>false</code>, which means that you can terminate the instance using the Amazon EC2 console, command line tools, or API. You can enable termination protection when you launch an instance, while the instance is running, or while the instance is stopped.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "aws_sdk_ec2.types.shutdown_behavior.ShutdownBehavior"
    ]
    """<p>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p> <p>Default: <code>stop</code> </p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet.</p> <p>Only one private IP address can be designated as primary. You can't specify this option if you've specified the option to designate a private IP address as the primary IP address in a network interface specification. You cannot specify this option if you're launching more than one instance in the request.</p> <p>You cannot specify this option and the network interfaces option in the same request.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p> <p>Constraints: Maximum 64 ASCII characters</p>"""
    additional_info: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_ec2.types.instance_network_interface_specification_list.InstanceNetworkInterfaceSpecificationList"
    ]
    """<p>The network interfaces to associate with the instance.</p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_specification.IamInstanceProfileSpecification"
    ]
    """<p>The name or Amazon Resource Name (ARN) of an IAM instance profile.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.</p> <p>Default: <code>false</code> </p>"""
