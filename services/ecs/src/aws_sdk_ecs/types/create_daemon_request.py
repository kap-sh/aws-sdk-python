"""Generated from Smithy shape ``com.amazonaws.ecs#CreateDaemonRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.daemon_deployment_configuration
    import aws_sdk_ecs.types.daemon_propagate_tags
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list
    import aws_sdk_ecs.types.tags


class CreateDaemonRequest(TypedDict):
    daemon_name: "aws_sdk_ecs.types.string.String"
    """<p>The name of the daemon. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster to create the daemon in.</p>"""
    daemon_task_definition_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon task definition to use for the daemon.</p>"""
    capacity_provider_arns: "aws_sdk_ecs.types.string_list.StringList"
    """<p>The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon. The daemon deploys tasks on container instances managed by these capacity providers.</p>"""
    deployment_configuration: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_configuration.DaemonDeploymentConfiguration"
    ]
    """<p>Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the daemon to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    propagate_tags: NotRequired[
        "aws_sdk_ecs.types.daemon_propagate_tags.DaemonPropagateTags"
    ]
    """<p>Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation. To add tags to a task after task creation, use the <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html\">TagResource</a> API action.</p>"""
    enable_ecs_managed_tags: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html\">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    enable_execute_command: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether the execute command functionality is turned on for the daemon. If <code>true</code>, the execute command functionality is turned on for all tasks in the daemon.</p>"""
    client_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDaemonRequest) -> dict:
    out: dict = {}
    out["daemonName"] = value["daemon_name"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    out["daemonTaskDefinitionArn"] = value["daemon_task_definition_arn"]
    import aws_sdk_ecs.types.string_list

    out["capacityProviderArns"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
        value["capacity_provider_arns"]
    )
    if "deployment_configuration" in value:
        import aws_sdk_ecs.types.daemon_deployment_configuration

        out["deploymentConfiguration"] = (
            aws_sdk_ecs.types.daemon_deployment_configuration.serialize_aws_json_1_1(
                value["deployment_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "propagate_tags" in value:
        import aws_sdk_ecs.types.daemon_propagate_tags

        out["propagateTags"] = (
            aws_sdk_ecs.types.daemon_propagate_tags.serialize_aws_json_1_1(
                value["propagate_tags"]
            )
        )
    out["enableECSManagedTags"] = value.get("enable_ecs_managed_tags", False)
    out["enableExecuteCommand"] = value.get("enable_execute_command", False)
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDaemonRequest:
    out: CreateDaemonRequest = {}  # type: ignore[typeddict-item]
    if "daemonName" in data:
        out["daemon_name"] = data["daemonName"]
    else:
        raise DeserializationError("CreateDaemonRequest.daemon_name required")
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "daemonTaskDefinitionArn" in data:
        out["daemon_task_definition_arn"] = data["daemonTaskDefinitionArn"]
    else:
        raise DeserializationError(
            "CreateDaemonRequest.daemon_task_definition_arn required"
        )
    if "capacityProviderArns" in data:
        import aws_sdk_ecs.types.string_list

        out["capacity_provider_arns"] = (
            aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
                data["capacityProviderArns"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDaemonRequest.capacity_provider_arns required"
        )
    if "deploymentConfiguration" in data:
        import aws_sdk_ecs.types.daemon_deployment_configuration

        out["deployment_configuration"] = (
            aws_sdk_ecs.types.daemon_deployment_configuration.deserialize_aws_json_1_1(
                data["deploymentConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if "propagateTags" in data:
        import aws_sdk_ecs.types.daemon_propagate_tags

        out["propagate_tags"] = (
            aws_sdk_ecs.types.daemon_propagate_tags.deserialize_aws_json_1_1(
                data["propagateTags"]
            )
        )
    if "enableECSManagedTags" in data:
        out["enable_ecs_managed_tags"] = data["enableECSManagedTags"]
    else:
        out["enable_ecs_managed_tags"] = False
    if "enableExecuteCommand" in data:
        out["enable_execute_command"] = data["enableExecuteCommand"]
    else:
        out["enable_execute_command"] = False
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
