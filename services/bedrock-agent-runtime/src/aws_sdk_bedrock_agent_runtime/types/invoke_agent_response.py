"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeAgentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.memory_id
    import aws_sdk_bedrock_agent_runtime.types.mime_type
    import aws_sdk_bedrock_agent_runtime.types.response_stream
    import aws_sdk_bedrock_agent_runtime.types.session_id


class InvokeAgentResponse(TypedDict, closed=True):
    completion: "aws_sdk_bedrock_agent_runtime.types.response_stream.ResponseStream"
    """<p>The agent's response to the user prompt.</p>"""
    content_type: "aws_sdk_bedrock_agent_runtime.types.mime_type.MimeType"
    """<p>The MIME type of the input data in the request. The default value is <code>application/json</code>.</p>"""
    session_id: "aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"
    """<p>The unique identifier of the session with the agent.</p>"""
    memory_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.memory_id.MemoryId"]
    """<p>The unique identifier of the agent memory.</p>"""
