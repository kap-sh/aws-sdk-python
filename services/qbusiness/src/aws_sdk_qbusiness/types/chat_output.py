"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.chat_output_stream

class ChatOutput(TypedDict):
    output_stream: NotRequired["aws_sdk_qbusiness.types.chat_output_stream.ChatOutputStream"]
    """<p>The streaming output for the <code>Chat</code> API.</p>"""