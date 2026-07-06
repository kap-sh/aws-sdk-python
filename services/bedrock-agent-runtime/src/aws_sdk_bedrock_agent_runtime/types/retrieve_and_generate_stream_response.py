"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_response_output
    import aws_sdk_bedrock_agent_runtime.types.session_id


class RetrieveAndGenerateStreamResponse(TypedDict, closed=True):
    stream: "aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_response_output.RetrieveAndGenerateStreamResponseOutput"
    """<p>A stream of events from the model.</p>"""
    session_id: "aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"
    """<p>The session ID.</p>"""
