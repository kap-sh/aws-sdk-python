"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.chat_output_stream


class ChatOutput(TypedDict, closed=True):
    output_stream: NotRequired[
        "aws_sdk_qbusiness.types.chat_output_stream.ChatOutputStream"
    ]
    """<p>The streaming output for the <code>Chat</code> API.</p>"""
