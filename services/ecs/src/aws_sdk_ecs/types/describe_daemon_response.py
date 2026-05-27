"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_detail


class DescribeDaemonResponse(TypedDict):
    daemon: NotRequired["aws_sdk_ecs.types.daemon_detail.DaemonDetail"]
    """<p>The full description of the daemon, including the current revisions, deployment ARN, cluster, and status information.</p>"""
