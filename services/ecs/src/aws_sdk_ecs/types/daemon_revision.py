"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonRevision``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.daemon_container_images
    import aws_sdk_ecs.types.daemon_propagate_tags
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DaemonRevision(TypedDict):
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
