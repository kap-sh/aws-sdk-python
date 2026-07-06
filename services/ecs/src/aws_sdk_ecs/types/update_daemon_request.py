"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateDaemonRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.daemon_deployment_configuration
    import aws_sdk_ecs.types.daemon_propagate_tags
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class UpdateDaemonRequest(TypedDict, closed=True):
    daemon_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon to update.</p>"""
    daemon_task_definition_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon task definition to use for the updated daemon.</p>"""
    capacity_provider_arns: "aws_sdk_ecs.types.string_list.StringList"
    """<p>The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon.</p>"""
    deployment_configuration: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_configuration.DaemonDeploymentConfiguration"
    ]
    """<p>Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.</p>"""
    propagate_tags: NotRequired[
        "aws_sdk_ecs.types.daemon_propagate_tags.DaemonPropagateTags"
    ]
    """<p>Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation.</p>"""
    enable_ecs_managed_tags: "aws_sdk_ecs.types.boolean.Boolean"
    r"""<p>Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html\">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    enable_execute_command: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>If <code>true</code>, the execute command functionality is turned on for all tasks in the daemon. If <code>false</code>, the execute command functionality is turned off.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDaemonRequest) -> dict:
    out: dict = {}
    out["daemonArn"] = value["daemon_arn"]
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
    if "propagate_tags" in value:
        import aws_sdk_ecs.types.daemon_propagate_tags

        out["propagateTags"] = (
            aws_sdk_ecs.types.daemon_propagate_tags.serialize_aws_json_1_1(
                value["propagate_tags"]
            )
        )
    out["enableECSManagedTags"] = value.get("enable_ecs_managed_tags", False)
    out["enableExecuteCommand"] = value.get("enable_execute_command", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDaemonRequest:
    out: UpdateDaemonRequest = {}  # type: ignore[typeddict-item]
    if "daemonArn" in data:
        out["daemon_arn"] = data["daemonArn"]
    else:
        raise DeserializationError("UpdateDaemonRequest.daemon_arn required")
    if "daemonTaskDefinitionArn" in data:
        out["daemon_task_definition_arn"] = data["daemonTaskDefinitionArn"]
    else:
        raise DeserializationError(
            "UpdateDaemonRequest.daemon_task_definition_arn required"
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
            "UpdateDaemonRequest.capacity_provider_arns required"
        )
    if "deploymentConfiguration" in data:
        import aws_sdk_ecs.types.daemon_deployment_configuration

        out["deployment_configuration"] = (
            aws_sdk_ecs.types.daemon_deployment_configuration.deserialize_aws_json_1_1(
                data["deploymentConfiguration"]
            )
        )
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
    return out
