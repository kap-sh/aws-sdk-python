"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#StopFlowExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_status


class StopFlowExecutionResponse(TypedDict):
    execution_arn: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the flow execution that was stopped.</p>"""
    status: (
        "aws_sdk_bedrock_agent_runtime.types.flow_execution_status.FlowExecutionStatus"
    )
    """<p>The updated status of the flow execution after the stop request. This will typically be ABORTED if the execution was successfully stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopFlowExecutionResponse) -> dict:
    out: dict = {}
    if "execution_arn" in value:
        out["executionArn"] = value["execution_arn"]
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_status

    out["status"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_execution_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> StopFlowExecutionResponse:
    out: StopFlowExecutionResponse = {}  # type: ignore[typeddict-item]
    if "executionArn" in data:
        out["execution_arn"] = data["executionArn"]
    if "status" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_execution_status

        out["status"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_execution_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("StopFlowExecutionResponse.status required")
    return out
