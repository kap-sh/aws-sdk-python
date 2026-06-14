"""Generated from Smithy shape ``com.amazonaws.eventbridge#EcsParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.arn
    import aws_sdk_eventbridge.types.boolean
    import aws_sdk_eventbridge.types.capacity_provider_strategy
    import aws_sdk_eventbridge.types.launch_type
    import aws_sdk_eventbridge.types.limit_min1
    import aws_sdk_eventbridge.types.network_configuration
    import aws_sdk_eventbridge.types.placement_constraints
    import aws_sdk_eventbridge.types.placement_strategies
    import aws_sdk_eventbridge.types.propagate_tags
    import aws_sdk_eventbridge.types.reference_id
    import aws_sdk_eventbridge.types.string
    import aws_sdk_eventbridge.types.tag_list


class EcsParameters(TypedDict):
    task_definition_arn: "aws_sdk_eventbridge.types.arn.Arn"
    """<p>The ARN of the task definition to use if the event target is an Amazon ECS task. </p>"""
    task_count: NotRequired["aws_sdk_eventbridge.types.limit_min1.LimitMin1"]
    """<p>The number of tasks to create based on <code>TaskDefinition</code>. The default is 1.</p>"""
    launch_type: NotRequired["aws_sdk_eventbridge.types.launch_type.LaunchType"]
    r"""<p>Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The <code>FARGATE</code> value is supported only in the Regions where Fargate with Amazon ECS is supported. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS-Fargate.html\">Fargate on Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    network_configuration: NotRequired[
        "aws_sdk_eventbridge.types.network_configuration.NetworkConfiguration"
    ]
    """<p>Use this structure if the Amazon ECS task uses the <code>awsvpc</code> network mode. This structure specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. This structure is required if <code>LaunchType</code> is <code>FARGATE</code> because the <code>awsvpc</code> mode is required for Fargate tasks.</p> <p>If you specify <code>NetworkConfiguration</code> when the target ECS task does not use the <code>awsvpc</code> network mode, the task fails.</p>"""
    platform_version: NotRequired["aws_sdk_eventbridge.types.string.String"]
    r"""<p>Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as <code>1.1.0</code>.</p> <p>This structure is used only if <code>LaunchType</code> is <code>FARGATE</code>. For more information about valid platform versions, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html\">Fargate Platform Versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    group: NotRequired["aws_sdk_eventbridge.types.string.String"]
    """<p>Specifies an ECS task group for the task. The maximum length is 255 characters.</p>"""
    capacity_provider_strategy: NotRequired[
        "aws_sdk_eventbridge.types.capacity_provider_strategy.CapacityProviderStrategy"
    ]
    """<p>The capacity provider strategy to use for the task.</p> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or launchType is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used. </p>"""
    enable_ecs_managed_tags: "aws_sdk_eventbridge.types.boolean.Boolean"
    r"""<p>Specifies whether to enable Amazon ECS managed tags for the task. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html\">Tagging Your Amazon ECS Resources</a> in the Amazon Elastic Container Service Developer Guide. </p>"""
    enable_execute_command: "aws_sdk_eventbridge.types.boolean.Boolean"
    """<p>Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task.</p>"""
    placement_constraints: NotRequired[
        "aws_sdk_eventbridge.types.placement_constraints.PlacementConstraints"
    ]
    """<p>An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).</p>"""
    placement_strategy: NotRequired[
        "aws_sdk_eventbridge.types.placement_strategies.PlacementStrategies"
    ]
    """<p>The placement strategy objects to use for the task. You can specify a maximum of five strategy rules per task. </p>"""
    propagate_tags: NotRequired[
        "aws_sdk_eventbridge.types.propagate_tags.PropagateTags"
    ]
    """<p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the TagResource API action. </p>"""
    reference_id: NotRequired["aws_sdk_eventbridge.types.reference_id.ReferenceId"]
    """<p>The reference ID to use for the task.</p>"""
    tags: NotRequired["aws_sdk_eventbridge.types.tag_list.TagList"]
    r"""<p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. To learn more, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html#ECS-RunTask-request-tags\">RunTask</a> in the Amazon ECS API Reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EcsParameters) -> dict:
    out: dict = {}
    out["TaskDefinitionArn"] = value["task_definition_arn"]
    if "task_count" in value:
        out["TaskCount"] = value["task_count"]
    if "launch_type" in value:
        import aws_sdk_eventbridge.types.launch_type

        out["LaunchType"] = (
            aws_sdk_eventbridge.types.launch_type.serialize_aws_json_1_1(
                value["launch_type"]
            )
        )
    if "network_configuration" in value:
        import aws_sdk_eventbridge.types.network_configuration

        out["NetworkConfiguration"] = (
            aws_sdk_eventbridge.types.network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "group" in value:
        out["Group"] = value["group"]
    if "capacity_provider_strategy" in value:
        import aws_sdk_eventbridge.types.capacity_provider_strategy

        out["CapacityProviderStrategy"] = (
            aws_sdk_eventbridge.types.capacity_provider_strategy.serialize_aws_json_1_1(
                value["capacity_provider_strategy"]
            )
        )
    out["EnableECSManagedTags"] = value.get("enable_ecs_managed_tags", False)
    out["EnableExecuteCommand"] = value.get("enable_execute_command", False)
    if "placement_constraints" in value:
        import aws_sdk_eventbridge.types.placement_constraints

        out["PlacementConstraints"] = (
            aws_sdk_eventbridge.types.placement_constraints.serialize_aws_json_1_1(
                value["placement_constraints"]
            )
        )
    if "placement_strategy" in value:
        import aws_sdk_eventbridge.types.placement_strategies

        out["PlacementStrategy"] = (
            aws_sdk_eventbridge.types.placement_strategies.serialize_aws_json_1_1(
                value["placement_strategy"]
            )
        )
    if "propagate_tags" in value:
        import aws_sdk_eventbridge.types.propagate_tags

        out["PropagateTags"] = (
            aws_sdk_eventbridge.types.propagate_tags.serialize_aws_json_1_1(
                value["propagate_tags"]
            )
        )
    if "reference_id" in value:
        out["ReferenceId"] = value["reference_id"]
    if "tags" in value:
        import aws_sdk_eventbridge.types.tag_list

        out["Tags"] = aws_sdk_eventbridge.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EcsParameters:
    out: EcsParameters = {}  # type: ignore[typeddict-item]
    if "TaskDefinitionArn" in data:
        out["task_definition_arn"] = data["TaskDefinitionArn"]
    else:
        raise DeserializationError("EcsParameters.task_definition_arn required")
    if "TaskCount" in data:
        out["task_count"] = data["TaskCount"]
    if "LaunchType" in data:
        import aws_sdk_eventbridge.types.launch_type

        out["launch_type"] = (
            aws_sdk_eventbridge.types.launch_type.deserialize_aws_json_1_1(
                data["LaunchType"]
            )
        )
    if "NetworkConfiguration" in data:
        import aws_sdk_eventbridge.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_eventbridge.types.network_configuration.deserialize_aws_json_1_1(
                data["NetworkConfiguration"]
            )
        )
    if "PlatformVersion" in data:
        out["platform_version"] = data["PlatformVersion"]
    if "Group" in data:
        out["group"] = data["Group"]
    if "CapacityProviderStrategy" in data:
        import aws_sdk_eventbridge.types.capacity_provider_strategy

        out["capacity_provider_strategy"] = (
            aws_sdk_eventbridge.types.capacity_provider_strategy.deserialize_aws_json_1_1(
                data["CapacityProviderStrategy"]
            )
        )
    if "EnableECSManagedTags" in data:
        out["enable_ecs_managed_tags"] = data["EnableECSManagedTags"]
    else:
        out["enable_ecs_managed_tags"] = False
    if "EnableExecuteCommand" in data:
        out["enable_execute_command"] = data["EnableExecuteCommand"]
    else:
        out["enable_execute_command"] = False
    if "PlacementConstraints" in data:
        import aws_sdk_eventbridge.types.placement_constraints

        out["placement_constraints"] = (
            aws_sdk_eventbridge.types.placement_constraints.deserialize_aws_json_1_1(
                data["PlacementConstraints"]
            )
        )
    if "PlacementStrategy" in data:
        import aws_sdk_eventbridge.types.placement_strategies

        out["placement_strategy"] = (
            aws_sdk_eventbridge.types.placement_strategies.deserialize_aws_json_1_1(
                data["PlacementStrategy"]
            )
        )
    if "PropagateTags" in data:
        import aws_sdk_eventbridge.types.propagate_tags

        out["propagate_tags"] = (
            aws_sdk_eventbridge.types.propagate_tags.deserialize_aws_json_1_1(
                data["PropagateTags"]
            )
        )
    if "ReferenceId" in data:
        out["reference_id"] = data["ReferenceId"]
    if "Tags" in data:
        import aws_sdk_eventbridge.types.tag_list

        out["tags"] = aws_sdk_eventbridge.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
