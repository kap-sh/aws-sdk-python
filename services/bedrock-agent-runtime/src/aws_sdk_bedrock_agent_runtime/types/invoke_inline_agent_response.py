"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeInlineAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.inline_agent_response_stream
    import aws_sdk_bedrock_agent_runtime.types.mime_type
    import aws_sdk_bedrock_agent_runtime.types.session_id


class InvokeInlineAgentResponse(TypedDict, closed=True):
    completion: "aws_sdk_bedrock_agent_runtime.types.inline_agent_response_stream.InlineAgentResponseStream"
    """<p>The inline agent's response to the user prompt. </p>"""
    content_type: "aws_sdk_bedrock_agent_runtime.types.mime_type.MimeType"
    """<p> The MIME type of the input data in the request. The default value is application/json. </p>"""
    session_id: "aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"
    """<p> The unique identifier of the session with the agent. </p>"""
