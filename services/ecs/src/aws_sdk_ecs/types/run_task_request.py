"""Generated from Smithy shape ``com.amazonaws.ecs#RunTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.capacity_provider_strategy
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.network_configuration
    import aws_sdk_ecs.types.placement_constraints
    import aws_sdk_ecs.types.placement_strategies
    import aws_sdk_ecs.types.propagate_tags
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tags
    import aws_sdk_ecs.types.task_override
    import aws_sdk_ecs.types.task_volume_configurations


class RunTaskRequest(TypedDict):
    capacity_provider_strategy: NotRequired[
        "aws_sdk_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy to use for the task.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>When you use cluster auto scaling, you must specify <code>capacityProviderStrategy</code> and not <code>launchType</code>. </p> <p>A capacity provider strategy can contain a maximum of 20 capacity providers.</p>"""
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster to run your task on. If you do not specify a cluster, the default cluster is assumed.</p> <p>Each account receives a default cluster the first time you use the service, but you may also create other clusters.</p>"""
    count: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks for each call.</p>"""
    enable_ecs_managed_tags: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Specifies whether to use Amazon ECS managed tags for the task. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html\">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    enable_execute_command: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to use the execute command functionality for the containers in this task. If <code>true</code>, this enables execute command functionality on all containers in the task.</p> <p>If <code>true</code>, then the task definition must have a task role, or you must provide one as an override.</p>"""
    group: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the task group to associate with the task. The default value is the family name of the task definition (for example, <code>family:my-family-name</code>).</p>"""
    launch_type: NotRequired["aws_sdk_ecs.types.launch_type.LaunchType"]
    """<p>The infrastructure to run your standalone task on. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html\">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>The <code>FARGATE</code> launch type runs your tasks on Fargate On-Demand infrastructure.</p> <note> <p>Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html\">Fargate capacity providers</a> in the <i>Amazon ECS Developer Guide</i>.</p> </note> <p>The <code>EC2</code> launch type runs your tasks on Amazon EC2 instances registered to your cluster.</p> <p>The <code>EXTERNAL</code> launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.</p> <p>A task can use either a launch type or a capacity provider strategy. If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p> <p>When you use cluster auto scaling, you must specify <code>capacityProviderStrategy</code> and not <code>launchType</code>. </p>"""
    network_configuration: NotRequired[
        "aws_sdk_ecs.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for the task. This parameter is required for task definitions that use the <code>awsvpc</code> network mode to receive their own elastic network interface, and it isn't supported for other network modes. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html\">Task networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    overrides: NotRequired["aws_sdk_ecs.types.task_override.TaskOverride"]
    """<p>A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that's specified in the task definition or Docker image) with a <code>command</code> override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an <code>environment</code> override.</p> <p>A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.</p>"""
    placement_constraints: NotRequired[
        "aws_sdk_ecs.types.placement_constraints.PlacementConstraints"
    ]
    """<p>An array of placement constraint objects to use for the task. You can specify up to 10 constraints for each task (including constraints in the task definition and those specified at runtime).</p>"""
    placement_strategy: NotRequired[
        "aws_sdk_ecs.types.placement_strategies.PlacementStrategies"
    ]
    """<p>The placement strategy objects to use for the task. You can specify a maximum of 5 strategy rules for each task.</p>"""
    platform_version: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The platform version the task uses. A platform version is only specified for tasks hosted on Fargate. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html\">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    propagate_tags: NotRequired["aws_sdk_ecs.types.propagate_tags.PropagateTags"]
    """<p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the<a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html\">TagResource</a> API action.</p> <note> <p>An error will be received if you specify the <code>SERVICE</code> option when running a task.</p> </note>"""
    reference_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>This parameter is only used by Amazon ECS. It is not intended for use by customers.</p>"""
    started_by: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the <code>startedBy</code> parameter. You can then identify which tasks belong to that job by filtering the results of a <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html\">ListTasks</a> call with the <code>startedBy</code> value. Up to 128 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (_) are allowed.</p> <p>If a task is started by an Amazon ECS service, then the <code>startedBy</code> parameter contains the deployment ID of the service that starts it.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    task_definition: "aws_sdk_ecs.types.string.String"
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p> <p>The full ARN value must match the value that you specified as the <code>Resource</code> of the principal's permissions policy.</p> <p>When you specify a task definition, you must either specify a specific revision, or all revisions in the ARN.</p> <p>To specify a specific revision, include the revision number in the ARN. For example, to specify revision 2, use <code>arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:2</code>.</p> <p>To specify all revisions, use the wildcard (*) in the ARN. For example, to specify all revisions, use <code>arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:*</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources\">Policy Resources for Amazon ECS</a> in the Amazon Elastic Container Service Developer Guide.</p>"""
    client_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 64 characters are allowed. The valid characters are characters in the range of 33-126, inclusive. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/ECS_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    volume_configurations: NotRequired[
        "aws_sdk_ecs.types.task_volume_configurations.TaskVolumeConfigurations"
    ]
    """<p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html\">TaskManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition.</p>"""
