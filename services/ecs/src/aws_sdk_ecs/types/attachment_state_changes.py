"""Generated from Smithy shape ``com.amazonaws.ecs#AttachmentStateChanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attachment_state_change

AttachmentStateChanges: TypeAlias = list[
    "aws_sdk_ecs.types.attachment_state_change.AttachmentStateChange"
]
