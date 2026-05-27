"""Generated from Smithy shape ``com.amazonaws.ec2#ResponseLaunchTemplateData``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.credit_specification
    import aws_sdk_ec2.types.elastic_gpu_specification_response_list
    import aws_sdk_ec2.types.instance_requirements
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.launch_template_block_device_mapping_list
    import aws_sdk_ec2.types.launch_template_capacity_reservation_specification_response
    import aws_sdk_ec2.types.launch_template_cpu_options
    import aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_response_list
    import aws_sdk_ec2.types.launch_template_enclave_options
    import aws_sdk_ec2.types.launch_template_hibernation_options
    import aws_sdk_ec2.types.launch_template_iam_instance_profile_specification
    import aws_sdk_ec2.types.launch_template_instance_maintenance_options
    import aws_sdk_ec2.types.launch_template_instance_market_options
    import aws_sdk_ec2.types.launch_template_instance_metadata_options
    import aws_sdk_ec2.types.launch_template_instance_network_interface_specification_list
    import aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification_list
    import aws_sdk_ec2.types.launch_template_license_list
    import aws_sdk_ec2.types.launch_template_network_performance_options
    import aws_sdk_ec2.types.launch_template_placement
    import aws_sdk_ec2.types.launch_template_private_dns_name_options
    import aws_sdk_ec2.types.launch_template_tag_specification_list
    import aws_sdk_ec2.types.launch_templates_monitoring
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.sensitive_user_data
    import aws_sdk_ec2.types.shutdown_behavior
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class ResponseLaunchTemplateData(TypedDict):
    kernel_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the kernel, if applicable.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is optimized for Amazon EBS I/O. </p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_ec2.types.launch_template_iam_instance_profile_specification.LaunchTemplateIamInstanceProfileSpecification"
    ]
    """<p>The IAM instance profile.</p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.launch_template_block_device_mapping_list.LaunchTemplateBlockDeviceMappingList"
    ]
    """<p>The block device mappings.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_network_interface_specification_list.LaunchTemplateInstanceNetworkInterfaceSpecificationList"
    ]
    """<p>The network interfaces.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the AMI or a Systems Manager parameter. The Systems Manager parameter will resolve to the ID of the AMI at instance launch.</p> <p>The value depends on what you specified in the request. The possible values are:</p> <ul> <li> <p>If an AMI ID was specified in the request, then this is the AMI ID.</p> </li> <li> <p>If a Systems Manager parameter was specified in the request, and <code>ResolveAlias</code> was configured as <code>true</code>, then this is the AMI ID that the parameter is mapped to in the Parameter Store.</p> </li> <li> <p>If a Systems Manager parameter was specified in the request, and <code>ResolveAlias</code> was configured as <code>false</code>, then this is the parameter value.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id\">Use a Systems Manager parameter instead of an AMI ID</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    key_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the key pair.</p>"""
    monitoring: NotRequired[
        "aws_sdk_ec2.types.launch_templates_monitoring.LaunchTemplatesMonitoring"
    ]
    """<p>The monitoring for the instance.</p>"""
    placement: NotRequired[
        "aws_sdk_ec2.types.launch_template_placement.LaunchTemplatePlacement"
    ]
    """<p>The placement of the instance.</p>"""
    ram_disk_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the RAM disk, if applicable.</p>"""
    disable_api_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If set to <code>true</code>, indicates that the instance cannot be terminated using the Amazon EC2 console, command line tool, or API.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "aws_sdk_ec2.types.shutdown_behavior.ShutdownBehavior"
    ]
    """<p>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p>"""
    user_data: NotRequired["aws_sdk_ec2.types.sensitive_user_data.SensitiveUserData"]
    """<p>The user data for the instance. </p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.launch_template_tag_specification_list.LaunchTemplateTagSpecificationList"
    ]
    """<p>The tags that are applied to the resources that are created during instance launch.</p>"""
    elastic_gpu_specifications: NotRequired[
        "aws_sdk_ec2.types.elastic_gpu_specification_response_list.ElasticGpuSpecificationResponseList"
    ]
    """<p>Deprecated.</p> <note> <p>Amazon Elastic Graphics reached end of life on January 8, 2024.</p> </note>"""
    elastic_inference_accelerators: NotRequired[
        "aws_sdk_ec2.types.launch_template_elastic_inference_accelerator_response_list.LaunchTemplateElasticInferenceAcceleratorResponseList"
    ]
    """<note> <p>Amazon Elastic Inference is no longer available.</p> </note> <p>An elastic inference accelerator to associate with the instance. Elastic inference accelerators are a resource you can attach to your Amazon EC2 instances to accelerate your Deep Learning (DL) inference workloads.</p> <p>You cannot specify accelerators from different generations in the same request.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The security group IDs.</p>"""
    security_groups: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The security group names.</p>"""
    instance_market_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_market_options.LaunchTemplateInstanceMarketOptions"
    ]
    """<p>The market (purchasing) option for the instances.</p>"""
    credit_specification: NotRequired[
        "aws_sdk_ec2.types.credit_specification.CreditSpecification"
    ]
    """<p>The credit option for CPU usage of the instance.</p>"""
    cpu_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_cpu_options.LaunchTemplateCpuOptions"
    ]
    """<p>The CPU options for the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html\">CPU options for Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    capacity_reservation_specification: NotRequired[
        "aws_sdk_ec2.types.launch_template_capacity_reservation_specification_response.LaunchTemplateCapacityReservationSpecificationResponse"
    ]
    """<p>Information about the Capacity Reservation targeting option.</p>"""
    license_specifications: NotRequired[
        "aws_sdk_ec2.types.launch_template_license_list.LaunchTemplateLicenseList"
    ]
    """<p>The license configurations.</p>"""
    hibernation_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_hibernation_options.LaunchTemplateHibernationOptions"
    ]
    """<p>Indicates whether an instance is configured for hibernation. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html\">Hibernate your Amazon EC2 instance</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    metadata_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_metadata_options.LaunchTemplateInstanceMetadataOptions"
    ]
    """<p>The metadata options for the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html\">Configure the Instance Metadata Service options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    enclave_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_enclave_options.LaunchTemplateEnclaveOptions"
    ]
    """<p>Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_ec2.types.instance_requirements.InstanceRequirements"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with these attributes.</p> <p>If you specify <code>InstanceRequirements</code>, you can't specify <code>InstanceTypes</code>.</p>"""
    private_dns_name_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_private_dns_name_options.LaunchTemplatePrivateDnsNameOptions"
    ]
    """<p>The options for the instance hostname.</p>"""
    maintenance_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_maintenance_options.LaunchTemplateInstanceMaintenanceOptions"
    ]
    """<p>The maintenance options for your instance.</p>"""
    disable_api_stop: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is enabled for stop protection. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html\">Enable stop protection for your EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The entity that manages the launch template.</p>"""
    network_performance_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_network_performance_options.LaunchTemplateNetworkPerformanceOptions"
    ]
    """<p>Contains the launch template settings for network performance options for your instance.</p>"""
    secondary_interfaces: NotRequired[
        "aws_sdk_ec2.types.launch_template_instance_secondary_interface_specification_list.LaunchTemplateInstanceSecondaryInterfaceSpecificationList"
    ]
    """<p>The secondary interfaces associated with the launch template.</p>"""
