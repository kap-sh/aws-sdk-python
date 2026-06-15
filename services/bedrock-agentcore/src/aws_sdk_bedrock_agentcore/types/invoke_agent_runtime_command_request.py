"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntimeCommandRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_request_body
    import aws_sdk_bedrock_agentcore.types.mime_type
    import aws_sdk_bedrock_agentcore.types.session_type


class InvokeAgentRuntimeCommandRequest(TypedDict):
    content_type: NotRequired["aws_sdk_bedrock_agentcore.types.mime_type.MimeType"]
    """<p>The MIME type of the input data in the request payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.</p>"""
    accept: NotRequired["aws_sdk_bedrock_agentcore.types.mime_type.MimeType"]
    """<p>The desired MIME type for the response from the agent runtime command. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.</p>"""
    runtime_session_id: NotRequired[
        "aws_sdk_bedrock_agentcore.types.session_type.SessionType"
    ]
    """<p>The unique identifier of the runtime session in which to execute the command. This session ID is used to maintain state and context across multiple command invocations.</p>"""
    trace_id: NotRequired["str"]
    """<p>The trace identifier for request tracking.</p>"""
    trace_parent: NotRequired["str"]
    """<p>The parent trace information for distributed tracing.</p>"""
    trace_state: NotRequired["str"]
    """<p>The trace state information for distributed tracing.</p>"""
    baggage: NotRequired["str"]
    """<p>Additional context information for distributed tracing.</p>"""
    agent_runtime_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the agent runtime on which to execute the command. This identifies the specific agent runtime environment where the command will run.</p>"""
    qualifier: NotRequired["str"]
    """<p>The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.</p>"""
    account_id: NotRequired["str"]
    """<p>The identifier of the Amazon Web Services account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for <code>agentRuntimeArn</code>.</p>"""
    body: "aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_request_body.InvokeAgentRuntimeCommandRequestBody"
    """<p>The request body containing the command to execute and optional configuration parameters such as timeout settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeAgentRuntimeCommandRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_request_body

    out["body"] = (
        aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_request_body.serialize_json(
            value["body"]
        )
    )
    return out


def deserialize_json(data: dict) -> InvokeAgentRuntimeCommandRequest:
    out: InvokeAgentRuntimeCommandRequest = {}  # type: ignore[typeddict-item]
    if "body" in data:
        import aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_request_body

        out["body"] = (
            aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_request_body.deserialize_json(
                data["body"]
            )
        )
    else:
        raise DeserializationError("InvokeAgentRuntimeCommandRequest.body required")
    return out
