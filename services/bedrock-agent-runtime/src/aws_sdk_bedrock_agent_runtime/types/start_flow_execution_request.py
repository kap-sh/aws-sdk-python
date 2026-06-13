"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#StartFlowExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_name
    import aws_sdk_bedrock_agent_runtime.types.flow_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_inputs
    import aws_sdk_bedrock_agent_runtime.types.model_performance_configuration


class StartFlowExecutionRequest(TypedDict):
    flow_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier"
    )
    """<p>The unique identifier of the flow to execute.</p>"""
    flow_alias_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the flow alias to use for the flow execution.</p>"""
    flow_execution_name: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_execution_name.FlowExecutionName"
    ]
    """<p>The unique name for the flow execution. If you don't provide one, a system-generated name is used.</p>"""
    inputs: "aws_sdk_bedrock_agent_runtime.types.flow_inputs.FlowInputs"
    """<p>The input data required for the flow execution. This must match the input schema defined in the flow.</p>"""
    model_performance_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
    ]
    """<p>The performance settings for the foundation model used in the flow execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartFlowExecutionRequest) -> dict:
    out: dict = {}
    if "flow_execution_name" in value:
        out["flowExecutionName"] = value["flow_execution_name"]
    import aws_sdk_bedrock_agent_runtime.types.flow_inputs

    out["inputs"] = aws_sdk_bedrock_agent_runtime.types.flow_inputs.serialize_json(
        value["inputs"]
    )
    if "model_performance_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.model_performance_configuration

        out["modelPerformanceConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.model_performance_configuration.serialize_json(
                value["model_performance_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartFlowExecutionRequest:
    out: StartFlowExecutionRequest = {}  # type: ignore[typeddict-item]
    if "flowExecutionName" in data:
        out["flow_execution_name"] = data["flowExecutionName"]
    if "inputs" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_inputs

        out["inputs"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_inputs.deserialize_json(
                data["inputs"]
            )
        )
    else:
        raise DeserializationError("StartFlowExecutionRequest.inputs required")
    if "modelPerformanceConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.model_performance_configuration

        out["model_performance_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.model_performance_configuration.deserialize_json(
                data["modelPerformanceConfiguration"]
            )
        )
    return out
