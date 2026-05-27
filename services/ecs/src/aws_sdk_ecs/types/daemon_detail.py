"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_revision_detail_list
    import aws_sdk_ecs.types.daemon_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DaemonDetail(TypedDict):
    daemon_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon.</p>"""
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster that the daemon is running in.</p>"""
    status: NotRequired["aws_sdk_ecs.types.daemon_status.DaemonStatus"]
    """<p>The status of the daemon.</p>"""
    current_revisions: NotRequired[
        "aws_sdk_ecs.types.daemon_revision_detail_list.DaemonRevisionDetailList"
    ]
    """<p>The current daemon revision details, including the running task counts per capacity provider.</p>"""
    deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the most recent daemon deployment.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was created.</p>"""
    updated_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was last updated.</p>"""
