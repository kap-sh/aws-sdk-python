"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevision``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.capacity_provider_strategy
    import aws_sdk_ecs.types.container_images
    import aws_sdk_ecs.types.deployment_ephemeral_storage
    import aws_sdk_ecs.types.ecs_managed_resources
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.load_balancers
    import aws_sdk_ecs.types.network_configuration
    import aws_sdk_ecs.types.resolved_configuration
    import aws_sdk_ecs.types.service_connect_configuration
    import aws_sdk_ecs.types.service_registries
    import aws_sdk_ecs.types.service_volume_configurations
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp
    import aws_sdk_ecs.types.vpc_lattice_configurations


class ServiceRevision(TypedDict):
    service_revision_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service revision.</p>"""
    service_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service for the service revision.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the cluster that hosts the service.</p>"""
    task_definition: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The task definition the service revision uses.</p>"""
    capacity_provider_strategy: NotRequired[
        "aws_sdk_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy the service revision uses.</p>"""
    launch_type: NotRequired["aws_sdk_ecs.types.launch_type.LaunchType"]
    """<p>The launch type the service revision uses.</p>"""
    platform_version: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>For the Fargate launch type, the platform version the service revision uses.</p>"""
    platform_family: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The platform family the service revision uses.</p>"""
    load_balancers: NotRequired["aws_sdk_ecs.types.load_balancers.LoadBalancers"]
    """<p>The load balancers the service revision uses.</p>"""
    service_registries: NotRequired[
        "aws_sdk_ecs.types.service_registries.ServiceRegistries"
    ]
    """<p>The service registries (for Service Discovery) the service revision uses.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_ecs.types.network_configuration.NetworkConfiguration"
    ]
    container_images: NotRequired["aws_sdk_ecs.types.container_images.ContainerImages"]
    """<p>The container images the service revision uses.</p>"""
    guard_duty_enabled: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Indicates whether Runtime Monitoring is turned on.</p>"""
    service_connect_configuration: NotRequired[
        "aws_sdk_ecs.types.service_connect_configuration.ServiceConnectConfiguration"
    ]
    volume_configurations: NotRequired[
        "aws_sdk_ecs.types.service_volume_configurations.ServiceVolumeConfigurations"
    ]
    """<p>The volumes that are configured at deployment that the service revision uses.</p>"""
    fargate_ephemeral_storage: NotRequired[
        "aws_sdk_ecs.types.deployment_ephemeral_storage.DeploymentEphemeralStorage"
    ]
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The time that the service revision was created. The format is yyyy-mm-dd HH:mm:ss.SSSSS.</p>"""
    vpc_lattice_configurations: NotRequired[
        "aws_sdk_ecs.types.vpc_lattice_configurations.VpcLatticeConfigurations"
    ]
    """<p>The VPC Lattice configuration for the service revision.</p>"""
    resolved_configuration: NotRequired[
        "aws_sdk_ecs.types.resolved_configuration.ResolvedConfiguration"
    ]
    """<p>The resolved configuration for the service revision which contains the actual resources your service revision uses, such as which target groups serve traffic.</p>"""
    ecs_managed_resources: NotRequired[
        "aws_sdk_ecs.types.ecs_managed_resources.ECSManagedResources"
    ]
    """<p>The resources created and managed by Amazon ECS when you create an Express service for Amazon ECS.</p>"""
