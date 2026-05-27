"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServiceRevisionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.service_revisions


class DescribeServiceRevisionsResponse(TypedDict):
    service_revisions: NotRequired[
        "aws_sdk_ecs.types.service_revisions.ServiceRevisions"
    ]
    """<p>The list of service revisions described.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
