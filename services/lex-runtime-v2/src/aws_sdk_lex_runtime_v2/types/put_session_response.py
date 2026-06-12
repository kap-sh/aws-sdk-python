"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#PutSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.blob_stream
    import aws_sdk_lex_runtime_v2.types.non_empty_string
    import aws_sdk_lex_runtime_v2.types.session_id


class PutSessionResponse(TypedDict):
    content_type: NotRequired[
        "aws_sdk_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of response. Same as the type specified in the <code>responseContentType</code> field in the request.</p>"""
    messages: NotRequired[
        "aws_sdk_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>A list of messages that were last sent to the user. The messages are ordered based on how you return the messages from you Lambda function or the order that the messages are defined in the bot.</p>"""
    session_state: NotRequired[
        "aws_sdk_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>A base-64-encoded gzipped field that represents the current state of the dialog between the user and the bot. Use this to determine the progress of the conversation and what the next action may be.</p>"""
    request_attributes: NotRequired[
        "aws_sdk_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>A base-64-encoded gzipped field that provides request-specific information passed between the client application and Amazon Lex V2. These are the same as the <code>requestAttribute</code> parameter in the call to the <code>PutSession</code> operation.</p>"""
    session_id: NotRequired["aws_sdk_lex_runtime_v2.types.session_id.SessionId"]
    """<p>The identifier of the session that received the data.</p>"""
    audio_stream: "aws_sdk_lex_runtime_v2.types.blob_stream.BlobStream"
    """<p>If the requested content type was audio, the audio version of the message to convey to the user.</p>"""
