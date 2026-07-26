"""Generated from Smithy shape ``com.amazonaws.guardduty#EcsTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.container_uids
    import capo_guardduty.types.ecs_launch_type
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class EcsTask(TypedDict, closed=True):
    created_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp indicating when the Amazon ECS task was created, in UTC format.</p>"""
    task_definition_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ARN of task definition which describes the container and volume definitions of the Amazon ECS task.</p>"""
    launch_type: NotRequired["capo_guardduty.types.ecs_launch_type.EcsLaunchType"]
    """<p>The infrastructure type on which the Amazon ECS task runs.</p>"""
    container_uids: NotRequired["capo_guardduty.types.container_uids.ContainerUids"]
    """<p>A list of unique identifiers for the containers associated with the Amazon ECS task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsTask) -> dict:
    out: dict = {}
    if "created_at" in value:
        import capo_guardduty.types.timestamp

        out["createdAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "task_definition_arn" in value:
        out["taskDefinitionArn"] = value["task_definition_arn"]
    if "launch_type" in value:
        import capo_guardduty.types.ecs_launch_type

        out["launchType"] = capo_guardduty.types.ecs_launch_type.serialize_json(
            value["launch_type"]
        )
    if "container_uids" in value:
        import capo_guardduty.types.container_uids

        out["containerUids"] = capo_guardduty.types.container_uids.serialize_json(
            value["container_uids"]
        )
    return out


def deserialize_json(data: dict) -> EcsTask:
    out: EcsTask = {}  # type: ignore[typeddict-item]
    if "createdAt" in data:
        import capo_guardduty.types.timestamp

        out["created_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "taskDefinitionArn" in data:
        out["task_definition_arn"] = data["taskDefinitionArn"]
    if "launchType" in data:
        import capo_guardduty.types.ecs_launch_type

        out["launch_type"] = capo_guardduty.types.ecs_launch_type.deserialize_json(
            data["launchType"]
        )
    if "containerUids" in data:
        import capo_guardduty.types.container_uids

        out["container_uids"] = capo_guardduty.types.container_uids.deserialize_json(
            data["containerUids"]
        )
    return out
