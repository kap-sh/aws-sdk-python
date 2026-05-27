"""Generated from Smithy shape ``com.amazonaws.ecs#AttachmentStateChange``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class AttachmentStateChange(TypedDict):
    attachment_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the attachment.</p>"""
    status: "aws_sdk_ecs.types.string.String"
    """<p>The status of the attachment.</p>"""
