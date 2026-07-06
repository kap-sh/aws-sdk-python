"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#StartFlowExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_identifier


class StartFlowExecutionResponse(TypedDict, closed=True):
    execution_arn: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the flow execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartFlowExecutionResponse) -> dict:
    out: dict = {}
    if "execution_arn" in value:
        out["executionArn"] = value["execution_arn"]
    return out


def deserialize_json(data: dict) -> StartFlowExecutionResponse:
    out: StartFlowExecutionResponse = {}  # type: ignore[typeddict-item]
    if "executionArn" in data:
        out["execution_arn"] = data["executionArn"]
    return out
