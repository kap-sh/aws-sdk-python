"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeCodeInterpreterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_id
    import aws_sdk_bedrock_agentcore.types.code_interpreter_stream_output


class InvokeCodeInterpreterResponse(TypedDict, closed=True):
    session_id: NotRequired[
        "aws_sdk_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
    ]
    """<p>The identifier of the code interpreter session.</p>"""
    stream: "aws_sdk_bedrock_agentcore.types.code_interpreter_stream_output.CodeInterpreterStreamOutput"
    """<p>The stream containing the results of the code execution. This includes output, errors, and execution status.</p>"""
