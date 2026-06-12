"""Generated from Smithy shape ``com.amazonaws.guardduty#EcsTaskDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.containers
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tags
    import aws_sdk_guardduty.types.timestamp
    import aws_sdk_guardduty.types.volumes


class EcsTaskDetails(TypedDict):
    arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task.</p>"""
    definition_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ARN of the task definition that creates the task.</p>"""
    version: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The version counter for the task.</p>"""
    task_created_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task was created.</p>"""
    started_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task started.</p>"""
    started_by: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Contains the tag specified when a task is started.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tags.Tags"]
    """<p>The tags of the ECS Task.</p>"""
    volumes: NotRequired["aws_sdk_guardduty.types.volumes.Volumes"]
    """<p>The list of data volume definitions for the task.</p>"""
    containers: NotRequired["aws_sdk_guardduty.types.containers.Containers"]
    """<p>The containers that's associated with the task.</p>"""
    group: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the task group that's associated with the task.</p>"""
    launch_type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>A capacity on which the task is running. For example, <code>Fargate</code> and <code>EC2</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsTaskDetails) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "definition_arn" in value:
        out["definitionArn"] = value["definition_arn"]
    if "version" in value:
        out["version"] = value["version"]
    if "task_created_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["createdAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["task_created_at"]
        )
    if "started_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["startedAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["started_at"]
        )
    if "started_by" in value:
        out["startedBy"] = value["started_by"]
    if "tags" in value:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.serialize_json(value["tags"])
    if "volumes" in value:
        import aws_sdk_guardduty.types.volumes

        out["volumes"] = aws_sdk_guardduty.types.volumes.serialize_json(
            value["volumes"]
        )
    if "containers" in value:
        import aws_sdk_guardduty.types.containers

        out["containers"] = aws_sdk_guardduty.types.containers.serialize_json(
            value["containers"]
        )
    if "group" in value:
        out["group"] = value["group"]
    if "launch_type" in value:
        out["launchType"] = value["launch_type"]
    return out


def deserialize_json(data: dict) -> EcsTaskDetails:
    out: EcsTaskDetails = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "definitionArn" in data:
        out["definition_arn"] = data["definitionArn"]
    if "version" in data:
        out["version"] = data["version"]
    if "createdAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["task_created_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "startedAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["started_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["startedAt"]
        )
    if "startedBy" in data:
        out["started_by"] = data["startedBy"]
    if "tags" in data:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.deserialize_json(data["tags"])
    if "volumes" in data:
        import aws_sdk_guardduty.types.volumes

        out["volumes"] = aws_sdk_guardduty.types.volumes.deserialize_json(
            data["volumes"]
        )
    if "containers" in data:
        import aws_sdk_guardduty.types.containers

        out["containers"] = aws_sdk_guardduty.types.containers.deserialize_json(
            data["containers"]
        )
    if "group" in data:
        out["group"] = data["group"]
    if "launchType" in data:
        out["launch_type"] = data["launchType"]
    return out
