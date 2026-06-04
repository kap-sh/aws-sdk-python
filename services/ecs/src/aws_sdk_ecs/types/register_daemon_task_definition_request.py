"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterDaemonTaskDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_container_definition_list
    import aws_sdk_ecs.types.daemon_volume_list
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tags


class RegisterDaemonTaskDefinitionRequest(TypedDict):
    family: "aws_sdk_ecs.types.string.String"
    """<p>You must specify a <code>family</code> for a daemon task definition. This family is used as a name for your daemon task definition. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>"""
    task_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this daemon task can assume. All containers in this daemon task are granted the permissions that are specified in this role.</p>"""
    execution_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. The task execution role is required for daemon tasks that pull container images from Amazon ECR or send container logs to CloudWatch.</p>"""
    container_definitions: "aws_sdk_ecs.types.daemon_container_definition_list.DaemonContainerDefinitionList"
    """<p>A list of container definitions in JSON format that describe the containers that make up your daemon task.</p>"""
    cpu: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The number of CPU units used by the daemon task. It can be expressed as an integer using CPU units (for example, <code>1024</code>).</p>"""
    memory: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The amount of memory (in MiB) used by the daemon task. It can be expressed as an integer using MiB (for example, <code>1024</code>).</p>"""
    volumes: NotRequired["aws_sdk_ecs.types.daemon_volume_list.DaemonVolumeList"]
    """<p>A list of volume definitions in JSON format that containers in your daemon task can use.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the daemon task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterDaemonTaskDefinitionRequest) -> dict:
    out: dict = {}
    out["family"] = value["family"]
    if "task_role_arn" in value:
        out["taskRoleArn"] = value["task_role_arn"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    import aws_sdk_ecs.types.daemon_container_definition_list

    out["containerDefinitions"] = (
        aws_sdk_ecs.types.daemon_container_definition_list.serialize_aws_json_1_1(
            value["container_definitions"]
        )
    )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "volumes" in value:
        import aws_sdk_ecs.types.daemon_volume_list

        out["volumes"] = aws_sdk_ecs.types.daemon_volume_list.serialize_aws_json_1_1(
            value["volumes"]
        )
    if "tags" in value:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterDaemonTaskDefinitionRequest:
    out: RegisterDaemonTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "family" in data:
        out["family"] = data["family"]
    else:
        raise DeserializationError(
            "RegisterDaemonTaskDefinitionRequest.family required"
        )
    if "taskRoleArn" in data:
        out["task_role_arn"] = data["taskRoleArn"]
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    if "containerDefinitions" in data:
        import aws_sdk_ecs.types.daemon_container_definition_list

        out["container_definitions"] = (
            aws_sdk_ecs.types.daemon_container_definition_list.deserialize_aws_json_1_1(
                data["containerDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterDaemonTaskDefinitionRequest.container_definitions required"
        )
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    if "memory" in data:
        out["memory"] = data["memory"]
    if "volumes" in data:
        import aws_sdk_ecs.types.daemon_volume_list

        out["volumes"] = aws_sdk_ecs.types.daemon_volume_list.deserialize_aws_json_1_1(
            data["volumes"]
        )
    if "tags" in data:
        import aws_sdk_ecs.types.tags

        out["tags"] = aws_sdk_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out
