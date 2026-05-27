"""Generated from Smithy shape ``com.amazonaws.ecs#TaskSet``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_provider_strategy
    import aws_sdk_ecs.types.deployment_ephemeral_storage
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.load_balancers
    import aws_sdk_ecs.types.network_configuration
    import aws_sdk_ecs.types.scale
    import aws_sdk_ecs.types.service_registries
    import aws_sdk_ecs.types.stability_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tags
    import aws_sdk_ecs.types.timestamp


class TaskSet(TypedDict):
    id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID of the task set.</p>"""
    task_set_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task set.</p>"""
    service_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service the task set exists in.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster that the service that hosts the task set exists in.</p>"""
    started_by: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The tag specified when a task set is started. If an CodeDeploy deployment created the task set, the <code>startedBy</code> parameter is <code>CODE_DEPLOY</code>. If an external deployment created the task set, the <code>startedBy</code> field isn't used.</p>"""
    external_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The external ID associated with the task set.</p> <p>If an CodeDeploy deployment created a task set, the <code>externalId</code> parameter contains the CodeDeploy deployment ID.</p> <p>If a task set is created for an external deployment and is associated with a service discovery registry, the <code>externalId</code> parameter contains the <code>ECS_TASK_SET_EXTERNAL_ID</code> Cloud Map attribute.</p>"""
    status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The status of the task set. The following describes each state.</p> <dl> <dt>PRIMARY</dt> <dd> <p>The task set is serving production traffic.</p> </dd> <dt>ACTIVE</dt> <dd> <p>The task set isn't serving production traffic.</p> </dd> <dt>DRAINING</dt> <dd> <p>The tasks in the task set are being stopped, and their corresponding targets are being deregistered from their target group.</p> </dd> </dl>"""
    task_definition: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The task definition that the task set is using.</p>"""
    computed_desired_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The computed desired count for the task set. This is calculated by multiplying the service's <code>desiredCount</code> by the task set's <code>scale</code> percentage. The result is always rounded up. For example, if the computed desired count is 1.2, it rounds up to 2 tasks.</p>"""
    pending_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of tasks in the task set that are in the <code>PENDING</code> status during a deployment. A task in the <code>PENDING</code> state is preparing to enter the <code>RUNNING</code> state. A task set enters the <code>PENDING</code> status when it launches for the first time or when it's restarted after being in the <code>STOPPED</code> state.</p>"""
    running_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of tasks in the task set that are in the <code>RUNNING</code> status during a deployment. A task in the <code>RUNNING</code> state is running and ready for use.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task set was created.</p>"""
    updated_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task set was last updated.</p>"""
    launch_type: NotRequired["aws_sdk_ecs.types.launch_type.LaunchType"]
    """<p>The launch type the tasks in the task set are using. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html\">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    capacity_provider_strategy: NotRequired[
        "aws_sdk_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy that are associated with the task set.</p>"""
    platform_version: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Fargate platform version where the tasks in the task set are running. A platform version is only specified for tasks run on Fargate. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html\">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    platform_family: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The operating system that your tasks in the set are running on. A platform family is specified only for tasks that use the Fargate launch type. </p> <p> All tasks in the set must have the same value.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_ecs.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for the task set.</p>"""
    load_balancers: NotRequired["aws_sdk_ecs.types.load_balancers.LoadBalancers"]
    """<p>Details on a load balancer that are used with a task set.</p>"""
    service_registries: NotRequired[
        "aws_sdk_ecs.types.service_registries.ServiceRegistries"
    ]
    """<p>The details for the service discovery registries to assign to this task set. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html\">Service discovery</a>.</p>"""
    scale: NotRequired["aws_sdk_ecs.types.scale.Scale"]
    """<p>A floating-point percentage of your desired number of tasks to place and keep running in the task set.</p>"""
    stability_status: NotRequired["aws_sdk_ecs.types.stability_status.StabilityStatus"]
    """<p>The stability status. This indicates whether the task set has reached a steady state. If the following conditions are met, the task set are in <code>STEADY_STATE</code>:</p> <ul> <li> <p>The task <code>runningCount</code> is equal to the <code>computedDesiredCount</code>.</p> </li> <li> <p>The <code>pendingCount</code> is <code>0</code>.</p> </li> <li> <p>There are no tasks that are running on container instances in the <code>DRAINING</code> status.</p> </li> <li> <p>All tasks are reporting a healthy status from the load balancers, service discovery, and container health checks.</p> </li> </ul> <p>If any of those conditions aren't met, the stability status returns <code>STABILIZING</code>.</p>"""
    stability_status_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task set stability status was retrieved.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the task set to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    fargate_ephemeral_storage: NotRequired[
        "aws_sdk_ecs.types.deployment_ephemeral_storage.DeploymentEphemeralStorage"
    ]
    """<p>The Fargate ephemeral storage settings for the task set.</p>"""
