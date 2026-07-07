"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.daemon_container_images
    import aws_sdk_ecs.types.daemon_propagate_tags
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DaemonRevision(TypedDict, closed=True):
    daemon_revision_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon revision.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster that hosts the daemon.</p>"""
    daemon_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon for this revision.</p>"""
    daemon_task_definition_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon task definition used by this revision.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon revision was created.</p>"""
    container_images: NotRequired[
        "aws_sdk_ecs.types.daemon_container_images.DaemonContainerImages"
    ]
    """<p>The container images used by the daemon revision.</p>"""
    propagate_tags: NotRequired[
        "aws_sdk_ecs.types.daemon_propagate_tags.DaemonPropagateTags"
    ]
    """<p>Specifies whether tags are propagated from the daemon to the daemon tasks.</p>"""
    enable_ecs_managed_tags: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether Amazon ECS managed tags are turned on for the daemon tasks.</p>"""
    enable_execute_command: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether the execute command functionality is turned on for the daemon tasks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonRevision) -> dict:
    out: dict = {}
    if "daemon_revision_arn" in value:
        out["daemonRevisionArn"] = value["daemon_revision_arn"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "daemon_arn" in value:
        out["daemonArn"] = value["daemon_arn"]
    if "daemon_task_definition_arn" in value:
        out["daemonTaskDefinitionArn"] = value["daemon_task_definition_arn"]
    if "created_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["createdAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "container_images" in value:
        import aws_sdk_ecs.types.daemon_container_images

        out["containerImages"] = (
            aws_sdk_ecs.types.daemon_container_images.serialize_aws_json_1_1(
                value["container_images"]
            )
        )
    if "propagate_tags" in value:
        import aws_sdk_ecs.types.daemon_propagate_tags

        out["propagateTags"] = (
            aws_sdk_ecs.types.daemon_propagate_tags.serialize_aws_json_1_1(
                value["propagate_tags"]
            )
        )
    if "enable_ecs_managed_tags" in value:
        out["enableECSManagedTags"] = value["enable_ecs_managed_tags"]
    if "enable_execute_command" in value:
        out["enableExecuteCommand"] = value["enable_execute_command"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonRevision:
    out: DaemonRevision = {}  # type: ignore[typeddict-item]
    if "daemonRevisionArn" in data:
        out["daemon_revision_arn"] = data["daemonRevisionArn"]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "daemonArn" in data:
        out["daemon_arn"] = data["daemonArn"]
    if "daemonTaskDefinitionArn" in data:
        out["daemon_task_definition_arn"] = data["daemonTaskDefinitionArn"]
    if "createdAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["created_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "containerImages" in data:
        import aws_sdk_ecs.types.daemon_container_images

        out["container_images"] = (
            aws_sdk_ecs.types.daemon_container_images.deserialize_aws_json_1_1(
                data["containerImages"]
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
    if "enableExecuteCommand" in data:
        out["enable_execute_command"] = data["enableExecuteCommand"]
    return out
