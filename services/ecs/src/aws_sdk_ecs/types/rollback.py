"""Generated from Smithy shape ``com.amazonaws.ecs#Rollback``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class Rollback(TypedDict):
    reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason the rollback happened. For example, the circuit breaker initiated the rollback operation.</p>"""
    started_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>Time time that the rollback started. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    service_revision_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the service revision deployed as part of the rollback.</p>"""
