"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceEvent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ServiceEvent(TypedDict):
    id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ID string for the event.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the event was triggered.</p>"""
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The event message.</p>"""
