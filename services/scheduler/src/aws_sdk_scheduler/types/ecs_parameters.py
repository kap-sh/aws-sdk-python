"""Generated from Smithy shape ``com.amazonaws.scheduler#EcsParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.capacity_provider_strategy
    import aws_sdk_scheduler.types.enable_ecs_managed_tags
    import aws_sdk_scheduler.types.enable_execute_command
    import aws_sdk_scheduler.types.group
    import aws_sdk_scheduler.types.launch_type
    import aws_sdk_scheduler.types.network_configuration
    import aws_sdk_scheduler.types.placement_constraints
    import aws_sdk_scheduler.types.placement_strategies
    import aws_sdk_scheduler.types.platform_version
    import aws_sdk_scheduler.types.propagate_tags
    import aws_sdk_scheduler.types.reference_id
    import aws_sdk_scheduler.types.tags
    import aws_sdk_scheduler.types.task_count
    import aws_sdk_scheduler.types.task_definition_arn


class EcsParameters(TypedDict):
    task_definition_arn: "aws_sdk_scheduler.types.task_definition_arn.TaskDefinitionArn"
    """<p>The Amazon Resource Name (ARN) of the task definition to use if the event target is an Amazon ECS task.</p>"""
    task_count: NotRequired["aws_sdk_scheduler.types.task_count.TaskCount"]
    """<p>The number of tasks to create based on <code>TaskDefinition</code>. The default is <code>1</code>.</p>"""
    launch_type: NotRequired["aws_sdk_scheduler.types.launch_type.LaunchType"]
    r"""<p>Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The <code>FARGATE</code> value is supported only in the Regions where Fargate with Amazon ECS is supported. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html\">AWS Fargate on Amazon ECS</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_scheduler.types.network_configuration.NetworkConfiguration"
    ]
    """<p>This structure specifies the network configuration for an ECS task.</p>"""
    platform_version: NotRequired[
        "aws_sdk_scheduler.types.platform_version.PlatformVersion"
    ]
    """<p>Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as <code>1.1.0</code>.</p>"""
    group: NotRequired["aws_sdk_scheduler.types.group.Group"]
    """<p>Specifies an ECS task group for the task. The maximum length is 255 characters.</p>"""
    capacity_provider_strategy: NotRequired[
        "aws_sdk_scheduler.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy to use for the task.</p>"""
    enable_ecs_managed_tags: NotRequired[
        "aws_sdk_scheduler.types.enable_ecs_managed_tags.EnableECSManagedTags"
    ]
    r"""<p>Specifies whether to enable Amazon ECS managed tags for the task. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html\">Tagging Your Amazon ECS Resources</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    enable_execute_command: NotRequired[
        "aws_sdk_scheduler.types.enable_execute_command.EnableExecuteCommand"
    ]
    """<p>Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task.</p>"""
    placement_constraints: NotRequired[
        "aws_sdk_scheduler.types.placement_constraints.PlacementConstraints"
    ]
    """<p>An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).</p>"""
    placement_strategy: NotRequired[
        "aws_sdk_scheduler.types.placement_strategies.PlacementStrategies"
    ]
    """<p>The task placement strategy for a task or service.</p>"""
    propagate_tags: NotRequired["aws_sdk_scheduler.types.propagate_tags.PropagateTags"]
    r"""<p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use Amazon ECS's <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html\"> <code>TagResource</code> </a> API action. </p>"""
    reference_id: NotRequired["aws_sdk_scheduler.types.reference_id.ReferenceId"]
    """<p>The reference ID to use for the task.</p>"""
    tags: NotRequired["aws_sdk_scheduler.types.tags.Tags"]
    r"""<p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html\"> <code>RunTask</code> </a> in the <i>Amazon ECS API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsParameters) -> dict:
    out: dict = {}
    out["TaskDefinitionArn"] = value["task_definition_arn"]
    if "task_count" in value:
        out["TaskCount"] = value["task_count"]
    if "launch_type" in value:
        out["LaunchType"] = value["launch_type"]
    if "network_configuration" in value:
        import aws_sdk_scheduler.types.network_configuration

        out["NetworkConfiguration"] = (
            aws_sdk_scheduler.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "group" in value:
        out["Group"] = value["group"]
    if "capacity_provider_strategy" in value:
        import aws_sdk_scheduler.types.capacity_provider_strategy

        out["CapacityProviderStrategy"] = (
            aws_sdk_scheduler.types.capacity_provider_strategy.serialize_json(
                value["capacity_provider_strategy"]
            )
        )
    if "enable_ecs_managed_tags" in value:
        out["EnableECSManagedTags"] = value["enable_ecs_managed_tags"]
    if "enable_execute_command" in value:
        out["EnableExecuteCommand"] = value["enable_execute_command"]
    if "placement_constraints" in value:
        import aws_sdk_scheduler.types.placement_constraints

        out["PlacementConstraints"] = (
            aws_sdk_scheduler.types.placement_constraints.serialize_json(
                value["placement_constraints"]
            )
        )
    if "placement_strategy" in value:
        import aws_sdk_scheduler.types.placement_strategies

        out["PlacementStrategy"] = (
            aws_sdk_scheduler.types.placement_strategies.serialize_json(
                value["placement_strategy"]
            )
        )
    if "propagate_tags" in value:
        out["PropagateTags"] = value["propagate_tags"]
    if "reference_id" in value:
        out["ReferenceId"] = value["reference_id"]
    if "tags" in value:
        import aws_sdk_scheduler.types.tags

        out["Tags"] = aws_sdk_scheduler.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EcsParameters:
    out: EcsParameters = {}  # type: ignore[typeddict-item]
    if "TaskDefinitionArn" in data:
        out["task_definition_arn"] = data["TaskDefinitionArn"]
    else:
        raise DeserializationError("EcsParameters.task_definition_arn required")
    if "TaskCount" in data:
        out["task_count"] = data["TaskCount"]
    if "LaunchType" in data:
        out["launch_type"] = data["LaunchType"]
    if "NetworkConfiguration" in data:
        import aws_sdk_scheduler.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_scheduler.types.network_configuration.deserialize_json(
                data["NetworkConfiguration"]
            )
        )
    if "PlatformVersion" in data:
        out["platform_version"] = data["PlatformVersion"]
    if "Group" in data:
        out["group"] = data["Group"]
    if "CapacityProviderStrategy" in data:
        import aws_sdk_scheduler.types.capacity_provider_strategy

        out["capacity_provider_strategy"] = (
            aws_sdk_scheduler.types.capacity_provider_strategy.deserialize_json(
                data["CapacityProviderStrategy"]
            )
        )
    if "EnableECSManagedTags" in data:
        out["enable_ecs_managed_tags"] = data["EnableECSManagedTags"]
    if "EnableExecuteCommand" in data:
        out["enable_execute_command"] = data["EnableExecuteCommand"]
    if "PlacementConstraints" in data:
        import aws_sdk_scheduler.types.placement_constraints

        out["placement_constraints"] = (
            aws_sdk_scheduler.types.placement_constraints.deserialize_json(
                data["PlacementConstraints"]
            )
        )
    if "PlacementStrategy" in data:
        import aws_sdk_scheduler.types.placement_strategies

        out["placement_strategy"] = (
            aws_sdk_scheduler.types.placement_strategies.deserialize_json(
                data["PlacementStrategy"]
            )
        )
    if "PropagateTags" in data:
        out["propagate_tags"] = data["PropagateTags"]
    if "ReferenceId" in data:
        out["reference_id"] = data["ReferenceId"]
    if "Tags" in data:
        import aws_sdk_scheduler.types.tags

        out["tags"] = aws_sdk_scheduler.types.tags.deserialize_json(data["Tags"])
    return out
