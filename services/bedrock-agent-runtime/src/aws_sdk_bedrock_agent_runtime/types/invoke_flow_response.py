"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeFlowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_id
    import aws_sdk_bedrock_agent_runtime.types.flow_response_stream


class InvokeFlowResponse(TypedDict):
    response_stream: (
        "aws_sdk_bedrock_agent_runtime.types.flow_response_stream.FlowResponseStream"
    )
    """<p>The output of the flow, returned as a stream. If there's an error, the error is returned.</p>"""
    execution_id: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_execution_id.FlowExecutionId"
    ]
    """<p>The unique identifier for the current flow execution.</p>"""
