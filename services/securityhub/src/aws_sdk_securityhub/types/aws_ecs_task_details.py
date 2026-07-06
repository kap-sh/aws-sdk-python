"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_container_details_list
    import aws_sdk_securityhub.types.aws_ecs_task_volume_details_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDetails(TypedDict, closed=True):
    cluster_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the cluster that hosts the task. </p>"""
    task_definition_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the task definition that creates the task. </p>"""
    version: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The version counter for the task. </p>"""
    created_at: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Unix timestamp for the time when the task was created. More specifically, it's for the time when the task entered the <code>PENDING</code> state. </p>"""
    started_at: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Unix timestamp for the time when the task started. More specifically, it's for the time when the task transitioned from the <code>PENDING</code> state to the <code>RUNNING</code> state. </p>"""
    started_by: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The tag specified when a task is started. If an Amazon ECS service started the task, the <code>startedBy</code> parameter contains the deployment ID of that service. </p>"""
    group: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the task group that's associated with the task. </p>"""
    volumes: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_task_volume_details_list.AwsEcsTaskVolumeDetailsList"
    ]
    """<p>Details about the data volume that is used in a task definition. </p>"""
    containers: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_container_details_list.AwsEcsContainerDetailsList"
    ]
    """<p>The containers that are associated with the task. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDetails) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "task_definition_arn" in value:
        out["TaskDefinitionArn"] = value["task_definition_arn"]
    if "version" in value:
        out["Version"] = value["version"]
    if "created_at" in value:
        out["CreatedAt"] = value["created_at"]
    if "started_at" in value:
        out["StartedAt"] = value["started_at"]
    if "started_by" in value:
        out["StartedBy"] = value["started_by"]
    if "group" in value:
        out["Group"] = value["group"]
    if "volumes" in value:
        import aws_sdk_securityhub.types.aws_ecs_task_volume_details_list

        out["Volumes"] = (
            aws_sdk_securityhub.types.aws_ecs_task_volume_details_list.serialize_json(
                value["volumes"]
            )
        )
    if "containers" in value:
        import aws_sdk_securityhub.types.aws_ecs_container_details_list

        out["Containers"] = (
            aws_sdk_securityhub.types.aws_ecs_container_details_list.serialize_json(
                value["containers"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEcsTaskDetails:
    out: AwsEcsTaskDetails = {}  # type: ignore[typeddict-item]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "TaskDefinitionArn" in data:
        out["task_definition_arn"] = data["TaskDefinitionArn"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "CreatedAt" in data:
        out["created_at"] = data["CreatedAt"]
    if "StartedAt" in data:
        out["started_at"] = data["StartedAt"]
    if "StartedBy" in data:
        out["started_by"] = data["StartedBy"]
    if "Group" in data:
        out["group"] = data["Group"]
    if "Volumes" in data:
        import aws_sdk_securityhub.types.aws_ecs_task_volume_details_list

        out["volumes"] = (
            aws_sdk_securityhub.types.aws_ecs_task_volume_details_list.deserialize_json(
                data["Volumes"]
            )
        )
    if "Containers" in data:
        import aws_sdk_securityhub.types.aws_ecs_container_details_list

        out["containers"] = (
            aws_sdk_securityhub.types.aws_ecs_container_details_list.deserialize_json(
                data["Containers"]
            )
        )
    return out
