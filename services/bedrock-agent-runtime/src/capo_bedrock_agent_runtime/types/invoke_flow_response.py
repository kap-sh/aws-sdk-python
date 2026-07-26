"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_execution_id
    import capo_bedrock_agent_runtime.types.flow_response_stream


class InvokeFlowResponse(TypedDict, closed=True):
    response_stream: (
        "capo_bedrock_agent_runtime.types.flow_response_stream.FlowResponseStream"
    )
    """<p>The output of the flow, returned as a stream. If there's an error, the error is returned.</p>"""
    execution_id: NotRequired[
        "capo_bedrock_agent_runtime.types.flow_execution_id.FlowExecutionId"
    ]
    """<p>The unique identifier for the current flow execution.</p>"""
