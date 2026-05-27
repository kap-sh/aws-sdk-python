"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceLaunchTemplate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.capacity_option_type
    import aws_sdk_ecs.types.capacity_reservation_request
    import aws_sdk_ecs.types.instance_requirements_request
    import aws_sdk_ecs.types.managed_instances_local_storage_configuration
    import aws_sdk_ecs.types.managed_instances_monitoring_options
    import aws_sdk_ecs.types.managed_instances_network_configuration
    import aws_sdk_ecs.types.managed_instances_storage_configuration
    import aws_sdk_ecs.types.string


class InstanceLaunchTemplate(TypedDict):
    ec2_instance_profile_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the instance profile that Amazon ECS applies to Amazon ECS Managed Instances. This instance profile must include the necessary permissions for your tasks to access Amazon Web Services services and resources.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-profile.html\">Amazon ECS instance profile for Managed Instances</a> in the <i>Amazon ECS Developer Guide</i>. </p>"""
    network_configuration: "aws_sdk_ecs.types.managed_instances_network_configuration.ManagedInstancesNetworkConfiguration"
    """<p>The network configuration for Amazon ECS Managed Instances. This specifies the subnets and security groups that instances use for network connectivity.</p>"""
    storage_configuration: NotRequired[
        "aws_sdk_ecs.types.managed_instances_storage_configuration.ManagedInstancesStorageConfiguration"
    ]
    """<p>The storage configuration for Amazon ECS Managed Instances. This defines the data volume properties for the instances.</p>"""
    local_storage_configuration: NotRequired[
        "aws_sdk_ecs.types.managed_instances_local_storage_configuration.ManagedInstancesLocalStorageConfiguration"
    ]
    """<p>The local storage configuration for Amazon ECS Managed Instances. This defines how ECS uses instance store volumes available on the container instance.</p>"""
    monitoring: NotRequired[
        "aws_sdk_ecs.types.managed_instances_monitoring_options.ManagedInstancesMonitoringOptions"
    ]
    """<p>CloudWatch provides two categories of monitoring: basic monitoring and detailed monitoring. By default, your managed instance is configured for basic monitoring. You can optionally enable detailed monitoring to help you more quickly identify and act on operational issues. You can enable or turn off detailed monitoring at launch or when the managed instance is running or stopped. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/detailed-monitoring-managed-instances.html\">Detailed monitoring for Amazon ECS Managed Instances</a> in the Amazon ECS Developer Guide.</p>"""
    capacity_option_type: NotRequired[
        "aws_sdk_ecs.types.capacity_option_type.CapacityOptionType"
    ]
    """<p>The capacity option type. This determines whether Amazon ECS launches On-Demand, Spot or Capacity Reservation Instances for your managed instance capacity provider.</p> <p>Valid values are:</p> <ul> <li> <p> <code>ON_DEMAND</code> - Launches standard On-Demand Instances. On-Demand Instances provide predictable pricing and availability.</p> </li> <li> <p> <code>SPOT</code> - Launches Spot Instances that use spare Amazon EC2 capacity at reduced cost. Spot Instances can be interrupted by Amazon EC2 with a two-minute notification when the capacity is needed back.</p> </li> <li> <p> <code>RESERVED</code> - Launches Instances using Amazon EC2 Capacity Reservations. Capacity Reservations allow you to reserve compute capacity for Amazon EC2 instances in a specific Availability Zone.</p> </li> </ul> <p>The default is On-Demand</p> <p>For more information about Amazon EC2 capacity options, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html\">Instance purchasing options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_metadata_tags_propagation: NotRequired[
        "aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Determines whether tags are propagated to the instance metadata service (IMDS) for Amazon EC2 instances launched by the Managed Instances capacity provider. When enabled, all tags associated with the instance are available through the instance metadata service. When disabled, tags are not propagated to IMDS.</p> <p>Disable this setting if your tags contain characters that are not compatible with IMDS, such as <code>/</code>. IMDS requires tag keys to match the pattern <code>[0-9a-zA-Z\-_+=,.@:]{1,255}</code>.</p> <p>The default value is <code>true</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#work-with-tags-in-IMDS\">Work with instance tags in instance metadata</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_ecs.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The instance requirements. You can specify:</p> <ul> <li> <p>The instance types</p> </li> <li> <p>Instance requirements such as vCPU count, memory, network performance, and accelerator specifications</p> </li> </ul> <p>Amazon ECS automatically selects the instances that match the specified criteria.</p>"""
    fips_enabled: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Determines whether to enable FIPS 140-2 validated cryptographic modules on EC2 instances launched by the capacity provider. If <code>true</code>, instances use FIPS-compliant cryptographic algorithms and modules for enhanced security compliance. If <code>false</code>, instances use standard cryptographic implementations.</p> <p>If not specified, instances are launched with FIPS enabled in Amazon Web Services GovCloud (US) regions and FIPS disabled in other regions.</p>"""
    capacity_reservations: NotRequired[
        "aws_sdk_ecs.types.capacity_reservation_request.CapacityReservationRequest"
    ]
    """<p>Capacity reservation specifications. You can specify:</p> <ul> <li> <p>Capacity reservation preference</p> </li> <li> <p>Reservation resource group to be used for targeted capacity reservations</p> </li> </ul> <p>Amazon ECS will launch instances according to the specified criteria.</p>"""
