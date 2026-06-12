"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#GetRawMessageContentResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmailmessageflow.types.message_content_blob


class GetRawMessageContentResponse(TypedDict):
    message_content: (
        "aws_sdk_workmailmessageflow.types.message_content_blob.messageContentBlob"
    )
    """<p>The raw content of the email message, in MIME format.</p>"""
