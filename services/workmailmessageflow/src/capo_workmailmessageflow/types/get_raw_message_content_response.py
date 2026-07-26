"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#GetRawMessageContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmailmessageflow.types.message_content_blob


class GetRawMessageContentResponse(TypedDict, closed=True):
    message_content: (
        "capo_workmailmessageflow.types.message_content_blob.messageContentBlob"
    )
    """<p>The raw content of the email message, in MIME format.</p>"""
