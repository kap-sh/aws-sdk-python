"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetFlowExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_identifier


class GetFlowExecutionRequest(TypedDict):
    flow_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier"
    )
    """<p>The unique identifier of the flow.</p>"""
    flow_alias_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the flow alias used for the execution.</p>"""
    execution_identifier: "aws_sdk_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier"
    """<p>The unique identifier of the flow execution to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFlowExecutionRequest:
    out: GetFlowExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
