"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_id
    import aws_sdk_bedrock_agent_runtime.types.flow_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_inputs
    import aws_sdk_bedrock_agent_runtime.types.model_performance_configuration


class InvokeFlowRequest(TypedDict):
    flow_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier"
    )
    """<p>The unique identifier of the flow.</p>"""
    flow_alias_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the flow alias.</p>"""
    inputs: "aws_sdk_bedrock_agent_runtime.types.flow_inputs.FlowInputs"
    """<p>A list of objects, each containing information about an input into the flow.</p>"""
    enable_trace: NotRequired["bool"]
    r"""<p>Specifies whether to return the trace for the flow or not. Traces track inputs and outputs for nodes in the flow. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html\">Track each step in your prompt flow by viewing its trace in Amazon Bedrock</a>.</p>"""
    model_performance_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
    ]
    """<p>Model performance settings for the request.</p>"""
    execution_id: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_execution_id.FlowExecutionId"
    ]
    """<p>The unique identifier for the current flow execution. If you don't provide a value, Amazon Bedrock creates the identifier for you. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeFlowRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.flow_inputs

    out["inputs"] = aws_sdk_bedrock_agent_runtime.types.flow_inputs.serialize_json(
        value["inputs"]
    )
    if "enable_trace" in value:
        out["enableTrace"] = value["enable_trace"]
    if "model_performance_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.model_performance_configuration

        out["modelPerformanceConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.model_performance_configuration.serialize_json(
                value["model_performance_configuration"]
            )
        )
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    return out


def deserialize_json(data: dict) -> InvokeFlowRequest:
    out: InvokeFlowRequest = {}  # type: ignore[typeddict-item]
    if "inputs" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_inputs

        out["inputs"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_inputs.deserialize_json(
                data["inputs"]
            )
        )
    else:
        raise DeserializationError("InvokeFlowRequest.inputs required")
    if "enableTrace" in data:
        out["enable_trace"] = data["enableTrace"]
    if "modelPerformanceConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.model_performance_configuration

        out["model_performance_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.model_performance_configuration.deserialize_json(
                data["modelPerformanceConfiguration"]
            )
        )
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    return out
