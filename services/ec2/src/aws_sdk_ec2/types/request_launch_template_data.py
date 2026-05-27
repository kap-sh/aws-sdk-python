"""Generated from Smithy shape ``com.amazonaws.ec2#RequestLaunchTemplateData``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.credit_specification_request
    import aws_sdk_ec2.types.elastic_gpu_specification_list
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.instance_requirements_request
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.kernel_id
    import aws_sdk_ec2.types.key_pair_name
    import aws_sdk_ec2.types.launch_template_block_device_mapping_request_list
    import aws_sdk_ec2.types.launch_template_capacity_reservation_specification_request
    import aws_sdk_ec2.types.launch_template_cpu_options_request
    import aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_list
    import aws_sdk_ec2.types.launch_template_enclave_options_request
    import aws_sdk_ec2.types.launch_template_hibernation_options_request
    import aws_sdk_ec2.types.launch_template_iam_instance_profile_specification_request
    import aws_sdk_ec2.types.launch_template_instance_maintenance_options_request
    import aws_sdk_ec2.types.launch_template_instance_market_options_request
    import aws_sdk_ec2.types.launch_template_instance_metadata_options_request
    import aws_sdk_ec2.types.launch_template_instance_network_interface_specification_request_list
    import aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification_request_list
    import aws_sdk_ec2.types.launch_template_license_specification_list_request
    import aws_sdk_ec2.types.launch_template_network_performance_options_request
    import aws_sdk_ec2.types.launch_template_placement_request
    import aws_sdk_ec2.types.launch_template_private_dns_name_options_request
    import aws_sdk_ec2.types.launch_template_tag_specification_request_list
    import aws_sdk_ec2.types.launch_templates_monitoring_request
    import aws_sdk_ec2.types.operator_request
    import aws_sdk_ec2.types.ramdisk_id
    import aws_sdk_ec2.types.security_group_id_string_list
    import aws_sdk_ec2.types.security_group_string_list
    import aws_sdk_ec2.types.sensitive_user_data
    import aws_sdk_ec2.types.shutdown_behavior


class RequestLaunchTemplateData(TypedDict):
    kernel_id: NotRequired["aws_sdk_ec2.types.kernel_id.KernelId"]
    """<p>The ID of the kernel.</p> <important> <p>We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href=\"https://docs.aws.amazon.com/linux/al2/ug/UserProvidedKernels.html\">User provided kernels</a> in the <i>Amazon Linux 2 User Guide</i>.</p> </important>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.</p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_ec2.types.launch_template_iam_instance_profile_specification_request.LaunchTemplateIamInstanceProfileSpecificationRequest"
    ]
    """<p>The name or Amazon Resource Name (ARN) of an IAM instance profile.</p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.launch_template_block_device_mapping_request_list.LaunchTemplateBlockDeviceMappingRequestList"
    ]
    """<p>The block device mapping.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_network_interface_specification_request_list.LaunchTemplateInstanceNetworkInterfaceSpecificationRequestList"
    ]
    """<p>The network interfaces for the instance.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI in the format <code>ami-0ac394d6a3example</code>.</p> <p>Alternatively, you can specify a Systems Manager parameter, using one of the following formats. The Systems Manager parameter will resolve to an AMI ID on launch.</p> <p>To reference a public parameter:</p> <ul> <li> <p> <code>resolve:ssm:<i>public-parameter</i> </code> </p> </li> </ul> <p>To reference a parameter stored in the same account:</p> <ul> <li> <p> <code>resolve:ssm:<i>parameter-name</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-name:version-number</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-name:label</i> </code> </p> </li> </ul> <p>To reference a parameter shared from another Amazon Web Services account:</p> <ul> <li> <p> <code>resolve:ssm:<i>parameter-ARN</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-ARN:version-number</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-ARN:label</i> </code> </p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id\">Use a Systems Manager parameter instead of an AMI ID</a> in the <i>Amazon EC2 User Guide</i>.</p> <note> <p>If the launch template will be used for an EC2 Fleet or Spot Fleet, note the following:</p> <ul> <li> <p>Only EC2 Fleets of type <code>instant</code> support specifying a Systems Manager parameter.</p> </li> <li> <p>For EC2 Fleets of type <code>maintain</code> or <code>request</code>, or for Spot Fleets, you must specify the AMI ID.</p> </li> </ul> </note>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html\">Amazon EC2 instance types</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>If you specify <code>InstanceType</code>, you can't specify <code>InstanceRequirements</code>.</p>"""
    key_name: NotRequired["aws_sdk_ec2.types.key_pair_name.KeyPairName"]
    """<p>The name of the key pair. You can create a key pair using <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateKeyPair.html\">CreateKeyPair</a> or <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportKeyPair.html\">ImportKeyPair</a>.</p> <important> <p>If you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.</p> </important>"""
    monitoring: NotRequired[
        "aws_sdk_ec2.types.launch_templates_monitoring_request.LaunchTemplatesMonitoringRequest"
    ]
    """<p>The monitoring for the instance.</p>"""
    placement: NotRequired[
        "aws_sdk_ec2.types.launch_template_placement_request.LaunchTemplatePlacementRequest"
    ]
    """<p>The placement for the instance.</p>"""
    ram_disk_id: NotRequired["aws_sdk_ec2.types.ramdisk_id.RamdiskId"]
    """<p>The ID of the RAM disk.</p> <important> <p>We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html\">User provided kernels</a> in the <i>Amazon EC2 User Guide</i>.</p> </important>"""
    disable_api_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether termination protection is enabled for the instance. The default is <code>false</code>, which means that you can terminate the instance using the Amazon EC2 console, command line tools, or API. You can enable termination protection when you launch an instance, while the instance is running, or while the instance is stopped.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "aws_sdk_ec2.types.shutdown_behavior.ShutdownBehavior"
    ]
    """<p>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p> <p>Default: <code>stop</code> </p>"""
    user_data: NotRequired["aws_sdk_ec2.types.sensitive_user_data.SensitiveUserData"]
    """<p>The user data to make available to the instance. You must provide base64-encoded text. User data is limited to 16 KB. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html\">Run commands when you launch an EC2 instance with user data input</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>If you are creating the launch template for use with Batch, the user data must be provided in the <a href=\"https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive\">MIME multi-part archive format</a>. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html#lt-user-data\">Amazon EC2 user data in launch templates</a> in the <i>Batch User Guide</i>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.launch_template_tag_specification_request_list.LaunchTemplateTagSpecificationRequestList"
    ]
    """<p>The tags to apply to the resources that are created during instance launch. These tags are not applied to the launch template.</p>"""
    elastic_gpu_specifications: NotRequired[
        "aws_sdk_ec2.types.elastic_gpu_specification_list.ElasticGpuSpecificationList"
    ]
    """<p>Deprecated.</p> <note> <p>Amazon Elastic Graphics reached end of life on January 8, 2024.</p> </note>"""
    elastic_inference_accelerators: NotRequired[
        "aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_list.LaunchTemplateElasticInferenceAcceleratorList"
    ]
    """<note> <p>Amazon Elastic Inference is no longer available.</p> </note> <p>An elastic inference accelerator to associate with the instance. Elastic inference accelerators are a resource you can attach to your Amazon EC2 instances to accelerate your Deep Learning (DL) inference workloads.</p> <p>You cannot specify accelerators from different generations in the same request.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>The IDs of the security groups.</p> <p>If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.</p>"""
    security_groups: NotRequired[
        "aws_sdk_ec2.types.security_group_string_list.SecurityGroupStringList"
    ]
    """<p>The names of the security groups. For a nondefault VPC, you must use security group IDs instead.</p> <p>If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.</p>"""
    instance_market_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_market_options_request.LaunchTemplateInstanceMarketOptionsRequest"
    ]
    """<p>The market (purchasing) option for the instances.</p>"""
    credit_specification: NotRequired[
        "aws_sdk_ec2.types.credit_specification_request.CreditSpecificationRequest"
    ]
    """<p>The credit option for CPU usage of the instance. Valid only for T instances.</p>"""
    cpu_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_cpu_options_request.LaunchTemplateCpuOptionsRequest"
    ]
    """<p>The CPU options for the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html\">CPU options for Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    capacity_reservation_specification: NotRequired[
        "aws_sdk_ec2.types.launch_template_capacity_reservation_specification_request.LaunchTemplateCapacityReservationSpecificationRequest"
    ]
    """<p>The Capacity Reservation targeting option. If you do not specify this parameter, the instance's Capacity Reservation preference defaults to <code>open</code>, which enables it to run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).</p>"""
    license_specifications: NotRequired[
        "aws_sdk_ec2.types.launch_template_license_specification_list_request.LaunchTemplateLicenseSpecificationListRequest"
    ]
    """<p>The license configurations.</p>"""
    hibernation_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_hibernation_options_request.LaunchTemplateHibernationOptionsRequest"
    ]
    """<p>Indicates whether an instance is enabled for hibernation. This parameter is valid only if the instance meets the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html\">hibernation prerequisites</a>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html\">Hibernate your Amazon EC2 instance</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    metadata_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_metadata_options_request.LaunchTemplateInstanceMetadataOptionsRequest"
    ]
    """<p>The metadata options for the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html\">Configure the Instance Metadata Service options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    enclave_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_enclave_options_request.LaunchTemplateEnclaveOptionsRequest"
    ]
    """<p>Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves. For more information, see <a href=\"https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html\">What is Nitro Enclaves?</a> in the <i>Amazon Web Services Nitro Enclaves User Guide</i>.</p> <p>You can't enable Amazon Web Services Nitro Enclaves and hibernation on the same instance.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_ec2.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with these attributes.</p> <p>You must specify <code>VCpuCount</code> and <code>MemoryMiB</code>. All other attributes are optional. Any unspecified optional attribute is set to its default.</p> <p>When you specify multiple attributes, you get instance types that satisfy all of the specified attributes. If you specify multiple values for an attribute, you get instance types that satisfy any of the specified values.</p> <p>To limit the list of instance types from which Amazon EC2 can identify matching instance types, you can use one of the following parameters, but not both in the same request:</p> <ul> <li> <p> <code>AllowedInstanceTypes</code> - The instance types to include in the list. All other instance types are ignored, even if they match your specified attributes.</p> </li> <li> <p> <code>ExcludedInstanceTypes</code> - The instance types to exclude from the list, even if they match your specified attributes.</p> </li> </ul> <note> <p>If you specify <code>InstanceRequirements</code>, you can't specify <code>InstanceType</code>.</p> <p>Attribute-based instance type selection is only supported when using Auto Scaling groups, EC2 Fleet, and Spot Fleet to launch instances. If you plan to use the launch template in the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html\">launch instance wizard</a>, or with the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html\">RunInstances</a> API or <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html\">AWS::EC2::Instance</a> Amazon Web Services CloudFormation resource, you can't specify <code>InstanceRequirements</code>.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html\">Specify attributes for instance type selection for EC2 Fleet or Spot Fleet</a> and <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html\">Spot placement score</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    private_dns_name_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_private_dns_name_options_request.LaunchTemplatePrivateDnsNameOptionsRequest"
    ]
    """<p>The options for the instance hostname. The default values are inherited from the subnet.</p>"""
    maintenance_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_maintenance_options_request.LaunchTemplateInstanceMaintenanceOptionsRequest"
    ]
    """<p>The maintenance options for the instance.</p>"""
    disable_api_stop: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to enable the instance for stop protection. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html\">Enable stop protection for your EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_request.OperatorRequest"]
    """<p>The entity that manages the launch template.</p>"""
    network_performance_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_network_performance_options_request.LaunchTemplateNetworkPerformanceOptionsRequest"
    ]
    """<p>Contains launch template settings to boost network performance for the type of workload that runs on your instance.</p>"""
    secondary_interfaces: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification_request_list.LaunchTemplateInstanceSecondaryInterfaceSpecificationRequestList"
    ]
    """<p>The secondary interfaces to associate with instances launched from the template.</p>"""
