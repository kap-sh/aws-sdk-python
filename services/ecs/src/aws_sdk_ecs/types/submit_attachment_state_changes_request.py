"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitAttachmentStateChangesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attachment_state_changes
    import aws_sdk_ecs.types.string


class SubmitAttachmentStateChangesRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full ARN of the cluster that hosts the container instance the attachment belongs to.</p>"""
    attachments: "aws_sdk_ecs.types.attachment_state_changes.AttachmentStateChanges"
    """<p>Any attachments associated with the state change request.</p>"""
