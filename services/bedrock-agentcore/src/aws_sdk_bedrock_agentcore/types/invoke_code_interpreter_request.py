"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeCodeInterpreterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_id
    import aws_sdk_bedrock_agentcore.types.tool_arguments
    import aws_sdk_bedrock_agentcore.types.tool_name


class InvokeCodeInterpreterRequest(TypedDict):
    code_interpreter_identifier: "str"
    """<p>The unique identifier of the code interpreter associated with the session. This must match the identifier used when creating the session with <code>StartCodeInterpreterSession</code>.</p>"""
    session_id: NotRequired[
        "aws_sdk_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
    ]
    """<p>The unique identifier of the code interpreter session to use. This must be an active session created with <code>StartCodeInterpreterSession</code>. If the session has expired or been stopped, the request will fail.</p>"""
    trace_id: NotRequired["str"]
    """<p>The trace identifier for request tracking.</p>"""
    trace_parent: NotRequired["str"]
    """<p>The parent trace information for distributed tracing.</p>"""
    name: "aws_sdk_bedrock_agentcore.types.tool_name.ToolName"
    """<p>The name of the code interpreter to invoke.</p>"""
    arguments: NotRequired[
        "aws_sdk_bedrock_agentcore.types.tool_arguments.ToolArguments"
    ]
    """<p>The arguments for the code interpreter. This includes the code to execute and any additional parameters such as the programming language, whether to clear the execution context, and other execution options. The structure of this parameter depends on the specific code interpreter being used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeCodeInterpreterRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.tool_name

    out["name"] = aws_sdk_bedrock_agentcore.types.tool_name.serialize_json(
        value["name"]
    )
    if "arguments" in value:
        import aws_sdk_bedrock_agentcore.types.tool_arguments

        out["arguments"] = (
            aws_sdk_bedrock_agentcore.types.tool_arguments.serialize_json(
                value["arguments"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvokeCodeInterpreterRequest:
    out: InvokeCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_bedrock_agentcore.types.tool_name

        out["name"] = aws_sdk_bedrock_agentcore.types.tool_name.deserialize_json(
            data["name"]
        )
    else:
        raise DeserializationError("InvokeCodeInterpreterRequest.name required")
    if "arguments" in data:
        import aws_sdk_bedrock_agentcore.types.tool_arguments

        out["arguments"] = (
            aws_sdk_bedrock_agentcore.types.tool_arguments.deserialize_json(
                data["arguments"]
            )
        )
    return out
