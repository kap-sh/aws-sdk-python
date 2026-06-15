"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeHarnessResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.invoke_harness_stream_output


class InvokeHarnessResponse(TypedDict):
    stream: "aws_sdk_bedrock_agentcore.types.invoke_harness_stream_output.InvokeHarnessStreamOutput"
    """<p>The streaming output from the harness invocation.</p>"""
