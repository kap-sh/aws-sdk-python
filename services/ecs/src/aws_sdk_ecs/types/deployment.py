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
