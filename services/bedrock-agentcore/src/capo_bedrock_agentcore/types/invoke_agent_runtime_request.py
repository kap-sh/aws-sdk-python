"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntimeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.body
    import capo_bedrock_agentcore.types.mime_type
    import capo_bedrock_agentcore.types.session_type
    import capo_bedrock_agentcore.types.string_type


class InvokeAgentRuntimeRequest(TypedDict, closed=True):
    content_type: NotRequired["capo_bedrock_agentcore.types.mime_type.MimeType"]
    """<p>The MIME type of the input data in the payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.</p>"""
    accept: NotRequired["capo_bedrock_agentcore.types.mime_type.MimeType"]
    """<p>The desired MIME type for the response from the agent runtime. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.</p>"""
    mcp_session_id: NotRequired["capo_bedrock_agentcore.types.string_type.StringType"]
    """<p>The identifier of the MCP session.</p>"""
    runtime_session_id: NotRequired[
        "capo_bedrock_agentcore.types.session_type.SessionType"
    ]
    """<p>The identifier of the runtime session.</p>"""
    mcp_protocol_version: NotRequired[
        "capo_bedrock_agentcore.types.string_type.StringType"
    ]
    """<p>The version of the MCP protocol being used.</p>"""
    runtime_user_id: NotRequired["capo_bedrock_agentcore.types.string_type.StringType"]
    """<p>The identifier of the runtime user.</p>"""
    trace_id: NotRequired["str"]
    """<p>The trace identifier for request tracking.</p>"""
    trace_parent: NotRequired["str"]
    """<p>The parent trace information for distributed tracing.</p>"""
    trace_state: NotRequired["str"]
    """<p>The trace state information for distributed tracing.</p>"""
    baggage: NotRequired["str"]
    """<p>Additional context information for distributed tracing.</p>"""
    agent_runtime_arn: "str"
    """<p>The identifier of the agent runtime to invoke. You can specify either the full Amazon Web Services Resource Name (ARN) or the agent ID. If you use the agent ID, you must also provide the <code>accountId</code> query parameter.</p>"""
    qualifier: NotRequired["str"]
    """<p>The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.</p>"""
    account_id: NotRequired["str"]
    """<p>The identifier of the Amazon Web Services account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for <code>agentRuntimeArn</code>.</p>"""
    payload: "capo_bedrock_agentcore.types.body.Body"
    """<p>The input data to send to the agent runtime. The format of this data depends on the specific agent configuration and must match the specified content type. For most agents, this is a JSON object containing the user's request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeAgentRuntimeRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.body

    out["payload"] = capo_bedrock_agentcore.types.body.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> InvokeAgentRuntimeRequest:
    out: InvokeAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
    if "payload" in data:
        import capo_bedrock_agentcore.types.body

        out["payload"] = capo_bedrock_agentcore.types.body.deserialize_json(
            data["payload"]
        )
    else:
        raise DeserializationError("InvokeAgentRuntimeRequest.payload required")
    return out
