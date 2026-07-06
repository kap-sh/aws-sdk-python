"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeHarnessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.invoke_harness_stream_output


class InvokeHarnessResponse(TypedDict, closed=True):
    stream: "aws_sdk_bedrock_agentcore.types.invoke_harness_stream_output.InvokeHarnessStreamOutput"
    """<p>The streaming output from the harness invocation.</p>"""
