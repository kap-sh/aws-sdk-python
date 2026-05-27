"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinition``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_container_definition_list
    import aws_sdk_ecs.types.daemon_task_definition_status
    import aws_sdk_ecs.types.daemon_volume_list
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DaemonTaskDefinition(TypedDict):
    daemon_task_definition_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The full Amazon Resource Name (ARN) of the daemon task definition.</p>"""
    family: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of a family that this daemon task definition is registered to.</p>"""
    revision: "aws_sdk_ecs.types.integer.Integer"
    """<p>The revision of the daemon task in a particular family. The revision is a version number of a daemon task definition in a family. When you register a daemon task definition for the first time, the revision is <code>1</code>. Each time that you register a new revision of a daemon task definition in the same family, the revision value always increases by one.</p>"""
    task_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the IAM role that grants containers in the daemon task permission to call Amazon Web Services APIs on your behalf.</p>"""
    execution_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf.</p>"""
    container_definitions: NotRequired[
        "aws_sdk_ecs.types.daemon_container_definition_list.DaemonContainerDefinitionList"
    ]
    """<p>A list of container definitions in JSON format that describe the containers that make up the daemon task.</p>"""
    volumes: NotRequired["aws_sdk_ecs.types.daemon_volume_list.DaemonVolumeList"]
    """<p>The list of data volume definitions for the daemon task.</p>"""
    cpu: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The number of CPU units used by the daemon task.</p>"""
    memory: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The amount of memory (in MiB) used by the daemon task.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.daemon_task_definition_status.DaemonTaskDefinitionStatus"
    ]
    """<p>The status of the daemon task definition. The valid values are <code>ACTIVE</code>, <code>DELETE_IN_PROGRESS</code>, and <code>DELETED</code>.</p>"""
    registered_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon task definition was registered.</p>"""
    delete_requested_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon task definition delete was requested.</p>"""
    registered_by: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The principal that registered the daemon task definition.</p>"""
