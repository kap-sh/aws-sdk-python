"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonRevisionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_revisions
    import aws_sdk_ecs.types.failures


class DescribeDaemonRevisionsResponse(TypedDict):
    daemon_revisions: NotRequired["aws_sdk_ecs.types.daemon_revisions.DaemonRevisions"]
    """<p>The list of daemon revisions.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
