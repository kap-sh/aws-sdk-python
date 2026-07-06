"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

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


class ServiceRevision(TypedDict, closed=True):
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRevision) -> dict:
    out: dict = {}
    if "service_revision_arn" in value:
        out["serviceRevisionArn"] = value["service_revision_arn"]
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "task_definition" in value:
        out["taskDefinition"] = value["task_definition"]
    if "capacity_provider_strategy" in value:
        import aws_sdk_ecs.types.capacity_provider_strategy

        out["capacityProviderStrategy"] = (
            aws_sdk_ecs.types.capacity_provider_strategy.serialize_aws_json_1_1(
                value["capacity_provider_strategy"]
            )
        )
    if "launch_type" in value:
        import aws_sdk_ecs.types.launch_type

        out["launchType"] = aws_sdk_ecs.types.launch_type.serialize_aws_json_1_1(
            value["launch_type"]
        )
    if "platform_version" in value:
        out["platformVersion"] = value["platform_version"]
    if "platform_family" in value:
        out["platformFamily"] = value["platform_family"]
    if "load_balancers" in value:
        import aws_sdk_ecs.types.load_balancers

        out["loadBalancers"] = aws_sdk_ecs.types.load_balancers.serialize_aws_json_1_1(
            value["load_balancers"]
        )
    if "service_registries" in value:
        import aws_sdk_ecs.types.service_registries

        out["serviceRegistries"] = (
            aws_sdk_ecs.types.service_registries.serialize_aws_json_1_1(
                value["service_registries"]
            )
        )
    if "network_configuration" in value:
        import aws_sdk_ecs.types.network_configuration

        out["networkConfiguration"] = (
            aws_sdk_ecs.types.network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "container_images" in value:
        import aws_sdk_ecs.types.container_images

        out["containerImages"] = (
            aws_sdk_ecs.types.container_images.serialize_aws_json_1_1(
                value["container_images"]
            )
        )
    out["guardDutyEnabled"] = value.get("guard_duty_enabled", False)
    if "service_connect_configuration" in value:
        import aws_sdk_ecs.types.service_connect_configuration

        out["serviceConnectConfiguration"] = (
            aws_sdk_ecs.types.service_connect_configuration.serialize_aws_json_1_1(
                value["service_connect_configuration"]
            )
        )
    if "volume_configurations" in value:
        import aws_sdk_ecs.types.service_volume_configurations

        out["volumeConfigurations"] = (
            aws_sdk_ecs.types.service_volume_configurations.serialize_aws_json_1_1(
                value["volume_configurations"]
            )
        )
    if "fargate_ephemeral_storage" in value:
        import aws_sdk_ecs.types.deployment_ephemeral_storage

        out["fargateEphemeralStorage"] = (
            aws_sdk_ecs.types.deployment_ephemeral_storage.serialize_aws_json_1_1(
                value["fargate_ephemeral_storage"]
            )
        )
    if "created_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["createdAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "vpc_lattice_configurations" in value:
        import aws_sdk_ecs.types.vpc_lattice_configurations

        out["vpcLatticeConfigurations"] = (
            aws_sdk_ecs.types.vpc_lattice_configurations.serialize_aws_json_1_1(
                value["vpc_lattice_configurations"]
            )
        )
    if "resolved_configuration" in value:
        import aws_sdk_ecs.types.resolved_configuration

        out["resolvedConfiguration"] = (
            aws_sdk_ecs.types.resolved_configuration.serialize_aws_json_1_1(
                value["resolved_configuration"]
            )
        )
    if "ecs_managed_resources" in value:
        import aws_sdk_ecs.types.ecs_managed_resources

        out["ecsManagedResources"] = (
            aws_sdk_ecs.types.ecs_managed_resources.serialize_aws_json_1_1(
                value["ecs_managed_resources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceRevision:
    out: ServiceRevision = {}  # type: ignore[typeddict-item]
    if "serviceRevisionArn" in data:
        out["service_revision_arn"] = data["serviceRevisionArn"]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "taskDefinition" in data:
        out["task_definition"] = data["taskDefinition"]
    if "capacityProviderStrategy" in data:
        import aws_sdk_ecs.types.capacity_provider_strategy

        out["capacity_provider_strategy"] = (
            aws_sdk_ecs.types.capacity_provider_strategy.deserialize_aws_json_1_1(
                data["capacityProviderStrategy"]
            )
        )
    if "launchType" in data:
        import aws_sdk_ecs.types.launch_type

        out["launch_type"] = aws_sdk_ecs.types.launch_type.deserialize_aws_json_1_1(
            data["launchType"]
        )
    if "platformVersion" in data:
        out["platform_version"] = data["platformVersion"]
    if "platformFamily" in data:
        out["platform_family"] = data["platformFamily"]
    if "loadBalancers" in data:
        import aws_sdk_ecs.types.load_balancers

        out["load_balancers"] = (
            aws_sdk_ecs.types.load_balancers.deserialize_aws_json_1_1(
                data["loadBalancers"]
            )
        )
    if "serviceRegistries" in data:
        import aws_sdk_ecs.types.service_registries

        out["service_registries"] = (
            aws_sdk_ecs.types.service_registries.deserialize_aws_json_1_1(
                data["serviceRegistries"]
            )
        )
    if "networkConfiguration" in data:
        import aws_sdk_ecs.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_ecs.types.network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if "containerImages" in data:
        import aws_sdk_ecs.types.container_images

        out["container_images"] = (
            aws_sdk_ecs.types.container_images.deserialize_aws_json_1_1(
                data["containerImages"]
            )
        )
    if "guardDutyEnabled" in data:
        out["guard_duty_enabled"] = data["guardDutyEnabled"]
    else:
        out["guard_duty_enabled"] = False
    if "serviceConnectConfiguration" in data:
        import aws_sdk_ecs.types.service_connect_configuration

        out["service_connect_configuration"] = (
            aws_sdk_ecs.types.service_connect_configuration.deserialize_aws_json_1_1(
                data["serviceConnectConfiguration"]
            )
        )
    if "volumeConfigurations" in data:
        import aws_sdk_ecs.types.service_volume_configurations

        out["volume_configurations"] = (
            aws_sdk_ecs.types.service_volume_configurations.deserialize_aws_json_1_1(
                data["volumeConfigurations"]
            )
        )
    if "fargateEphemeralStorage" in data:
        import aws_sdk_ecs.types.deployment_ephemeral_storage

        out["fargate_ephemeral_storage"] = (
            aws_sdk_ecs.types.deployment_ephemeral_storage.deserialize_aws_json_1_1(
                data["fargateEphemeralStorage"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["created_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "vpcLatticeConfigurations" in data:
        import aws_sdk_ecs.types.vpc_lattice_configurations

        out["vpc_lattice_configurations"] = (
            aws_sdk_ecs.types.vpc_lattice_configurations.deserialize_aws_json_1_1(
                data["vpcLatticeConfigurations"]
            )
        )
    if "resolvedConfiguration" in data:
        import aws_sdk_ecs.types.resolved_configuration

        out["resolved_configuration"] = (
            aws_sdk_ecs.types.resolved_configuration.deserialize_aws_json_1_1(
                data["resolvedConfiguration"]
            )
        )
    if "ecsManagedResources" in data:
        import aws_sdk_ecs.types.ecs_managed_resources

        out["ecs_managed_resources"] = (
            aws_sdk_ecs.types.ecs_managed_resources.deserialize_aws_json_1_1(
                data["ecsManagedResources"]
            )
        )
    return out
