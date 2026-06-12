"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StartConversationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.start_conversation_response_event_stream


class StartConversationResponse(TypedDict):
    response_event_stream: NotRequired[
        "aws_sdk_lex_runtime_v2.types.start_conversation_response_event_stream.StartConversationResponseEventStream"
    ]
    """<p>Represents the stream of events from Amazon Lex V2 to your application. The events are encoded as HTTP/2 data frames.</p>"""
