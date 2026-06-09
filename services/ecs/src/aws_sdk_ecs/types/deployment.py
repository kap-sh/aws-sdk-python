"""Generated from Smithy shape ``com.amazonaws.ecs#Deployment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_provider_strategy
    import aws_sdk_ecs.types.deployment_ephemeral_storage
    import aws_sdk_ecs.types.deployment_rollout_state
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.network_configuration
    import aws_sdk_ecs.types.service_connect_configuration
    import aws_sdk_ecs.types.service_connect_service_resource_list
    import aws_sdk_ecs.types.service_volume_configurations
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp
    import aws_sdk_ecs.types.vpc_lattice_configurations


class Deployment(TypedDict):
    id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID of the deployment.</p>"""
    status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The status of the deployment. The following describes each state.</p> <dl> <dt>PRIMARY</dt> <dd> <p>The most recent deployment of a service.</p> </dd> <dt>ACTIVE</dt> <dd> <p>A service deployment that still has running tasks, but are in the process of being replaced with a new <code>PRIMARY</code> deployment.</p> </dd> <dt>INACTIVE</dt> <dd> <p>A deployment that has been completely replaced.</p> </dd> </dl>"""
    task_definition: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The most recent task definition that was specified for the tasks in the service to use.</p>"""
    desired_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The most recent desired count of tasks that was specified for the service to deploy or maintain.</p>"""
    pending_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of tasks in the deployment that are in the <code>PENDING</code> status.</p>"""
    running_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of tasks in the deployment that are in the <code>RUNNING</code> status.</p>"""
    failed_tasks: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of consecutively failed tasks in the deployment. A task is considered a failure if the service scheduler can't launch the task, the task doesn't transition to a <code>RUNNING</code> state, or if it fails any of its defined health checks and is stopped.</p> <note> <p>Once a service deployment has one or more successfully running tasks, the failed task count resets to zero and stops being evaluated.</p> </note>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the service deployment was created.</p>"""
    updated_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the service deployment was last updated.</p>"""
    capacity_provider_strategy: NotRequired[
        "aws_sdk_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy that the deployment is using.</p>"""
    launch_type: NotRequired["aws_sdk_ecs.types.launch_type.LaunchType"]
    """<p>The launch type the tasks in the service are using. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html\">Amazon ECS Launch Types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    platform_version: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The platform version that your tasks in the service run on. A platform version is only specified for tasks using the Fargate launch type. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html\">Fargate Platform Versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    platform_family: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The operating system that your tasks in the service, or tasks are running on. A platform family is specified only for tasks using the Fargate launch type. </p> <p> All tasks that run as part of this service must use the same <code>platformFamily</code> value as the service, for example, <code> LINUX.</code>.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_ecs.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the <code>awsvpc</code> networking mode.</p>"""
    rollout_state: NotRequired[
        "aws_sdk_ecs.types.deployment_rollout_state.DeploymentRolloutState"
    ]
    """<note> <p>The <code>rolloutState</code> of a service is only returned for services that use the rolling update (<code>ECS</code>) deployment type that aren't behind a Classic Load Balancer.</p> </note> <p>The rollout state of the deployment. When a service deployment is started, it begins in an <code>IN_PROGRESS</code> state. When the service reaches a steady state, the deployment transitions to a <code>COMPLETED</code> state. If the service fails to reach a steady state and circuit breaker is turned on, the deployment transitions to a <code>FAILED</code> state. A deployment in <code>FAILED</code> state doesn't launch any new tasks. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeploymentCircuitBreaker.html\">DeploymentCircuitBreaker</a>.</p>"""
    rollout_state_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>A description of the rollout state of a deployment.</p>"""
    service_connect_configuration: NotRequired[
        "aws_sdk_ecs.types.service_connect_configuration.ServiceConnectConfiguration"
    ]
    """<p>The details of the Service Connect configuration that's used by this deployment. Compare the configuration between multiple deployments when troubleshooting issues with new deployments.</p> <p>The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html\">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    service_connect_resources: NotRequired[
        "aws_sdk_ecs.types.service_connect_service_resource_list.ServiceConnectServiceResourceList"
    ]
    """<p>The list of Service Connect resources that are associated with this deployment. Each list entry maps a discovery name to a Cloud Map service name.</p>"""
    volume_configurations: NotRequired[
        "aws_sdk_ecs.types.service_volume_configurations.ServiceVolumeConfigurations"
    ]
    """<p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure different settings like the size, throughput, volumeType, and ecryption in <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceManagedEBSVolumeConfiguration.html\">ServiceManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition.</p>"""
    fargate_ephemeral_storage: NotRequired[
        "aws_sdk_ecs.types.deployment_ephemeral_storage.DeploymentEphemeralStorage"
    ]
    """<p>The Fargate ephemeral storage settings for the deployment.</p>"""
    vpc_lattice_configurations: NotRequired[
        "aws_sdk_ecs.types.vpc_lattice_configurations.VpcLatticeConfigurations"
    ]
    """<p>The VPC Lattice configuration for the service deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Deployment) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "status" in value:
        out["status"] = value["status"]
    if "task_definition" in value:
        out["taskDefinition"] = value["task_definition"]
    out["desiredCount"] = value.get("desired_count", 0)
    out["pendingCount"] = value.get("pending_count", 0)
    out["runningCount"] = value.get("running_count", 0)
    out["failedTasks"] = value.get("failed_tasks", 0)
    if "created_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["createdAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["updatedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
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
    if "network_configuration" in value:
        import aws_sdk_ecs.types.network_configuration

        out["networkConfiguration"] = (
            aws_sdk_ecs.types.network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "rollout_state" in value:
        import aws_sdk_ecs.types.deployment_rollout_state

        out["rolloutState"] = (
            aws_sdk_ecs.types.deployment_rollout_state.serialize_aws_json_1_1(
                value["rollout_state"]
            )
        )
    if "rollout_state_reason" in value:
        out["rolloutStateReason"] = value["rollout_state_reason"]
    if "service_connect_configuration" in value:
        import aws_sdk_ecs.types.service_connect_configuration

        out["serviceConnectConfiguration"] = (
            aws_sdk_ecs.types.service_connect_configuration.serialize_aws_json_1_1(
                value["service_connect_configuration"]
            )
        )
    if "service_connect_resources" in value:
        import aws_sdk_ecs.types.service_connect_service_resource_list

        out["serviceConnectResources"] = (
            aws_sdk_ecs.types.service_connect_service_resource_list.serialize_aws_json_1_1(
                value["service_connect_resources"]
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
    if "vpc_lattice_configurations" in value:
        import aws_sdk_ecs.types.vpc_lattice_configurations

        out["vpcLatticeConfigurations"] = (
            aws_sdk_ecs.types.vpc_lattice_configurations.serialize_aws_json_1_1(
                value["vpc_lattice_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Deployment:
    out: Deployment = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "status" in data:
        out["status"] = data["status"]
    if "taskDefinition" in data:
        out["task_definition"] = data["taskDefinition"]
    if "desiredCount" in data:
        out["desired_count"] = data["desiredCount"]
    else:
        out["desired_count"] = 0
    if "pendingCount" in data:
        out["pending_count"] = data["pendingCount"]
    else:
        out["pending_count"] = 0
    if "runningCount" in data:
        out["running_count"] = data["runningCount"]
    else:
        out["running_count"] = 0
    if "failedTasks" in data:
        out["failed_tasks"] = data["failedTasks"]
    else:
        out["failed_tasks"] = 0
    if "createdAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["created_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["updated_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["updatedAt"]
        )
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
    if "networkConfiguration" in data:
        import aws_sdk_ecs.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_ecs.types.network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if "rolloutState" in data:
        import aws_sdk_ecs.types.deployment_rollout_state

        out["rollout_state"] = (
            aws_sdk_ecs.types.deployment_rollout_state.deserialize_aws_json_1_1(
                data["rolloutState"]
            )
        )
    if "rolloutStateReason" in data:
        out["rollout_state_reason"] = data["rolloutStateReason"]
    if "serviceConnectConfiguration" in data:
        import aws_sdk_ecs.types.service_connect_configuration

        out["service_connect_configuration"] = (
            aws_sdk_ecs.types.service_connect_configuration.deserialize_aws_json_1_1(
                data["serviceConnectConfiguration"]
            )
        )
    if "serviceConnectResources" in data:
        import aws_sdk_ecs.types.service_connect_service_resource_list

        out["service_connect_resources"] = (
            aws_sdk_ecs.types.service_connect_service_resource_list.deserialize_aws_json_1_1(
                data["serviceConnectResources"]
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
    if "vpcLatticeConfigurations" in data:
        import aws_sdk_ecs.types.vpc_lattice_configurations

        out["vpc_lattice_configurations"] = (
            aws_sdk_ecs.types.vpc_lattice_configurations.deserialize_aws_json_1_1(
                data["vpcLatticeConfigurations"]
            )
        )
    return out
