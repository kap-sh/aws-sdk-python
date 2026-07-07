"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntimeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.http_response_code
    import aws_sdk_bedrock_agentcore.types.response_stream
    import aws_sdk_bedrock_agentcore.types.session_id


class InvokeAgentRuntimeResponse(TypedDict, closed=True):
    runtime_session_id: NotRequired[
        "aws_sdk_bedrock_agentcore.types.session_id.SessionId"
    ]
    """<p>The identifier of the runtime session.</p>"""
    mcp_session_id: NotRequired["aws_sdk_bedrock_agentcore.types.session_id.SessionId"]
    """<p>The identifier of the MCP session.</p>"""
    mcp_protocol_version: NotRequired["str"]
    """<p>The version of the MCP protocol being used.</p>"""
    trace_id: NotRequired["str"]
    """<p>The trace identifier for request tracking.</p>"""
    trace_parent: NotRequired["str"]
    """<p>The parent trace information for distributed tracing.</p>"""
    trace_state: NotRequired["str"]
    """<p>The trace state information for distributed tracing.</p>"""
    baggage: NotRequired["str"]
    """<p>Additional context information for distributed tracing.</p>"""
    content_type: "str"
    """<p>The MIME type of the response data. This indicates how to interpret the response data. Common values include application/json for JSON data.</p>"""
    response: "aws_sdk_bedrock_agentcore.types.response_stream.ResponseStream"
    """<p>The response data from the agent runtime. The format of this data depends on the specific agent configuration and the requested accept type. For most agents, this is a JSON object containing the agent's response to the user's request.</p>"""
    status_code: NotRequired[
        "aws_sdk_bedrock_agentcore.types.http_response_code.HttpResponseCode"
    ]
    """<p>The HTTP status code of the response. A status code of 200 indicates a successful operation. Other status codes indicate various error conditions.</p>"""
