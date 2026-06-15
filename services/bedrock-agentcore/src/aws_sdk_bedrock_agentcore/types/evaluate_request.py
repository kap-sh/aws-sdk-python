"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluation_input
    import aws_sdk_bedrock_agentcore.types.evaluation_reference_inputs
    import aws_sdk_bedrock_agentcore.types.evaluation_target
    import aws_sdk_bedrock_agentcore.types.evaluator_id


class EvaluateRequest(TypedDict):
    evaluator_id: "aws_sdk_bedrock_agentcore.types.evaluator_id.EvaluatorId"
    """<p> The unique identifier of the evaluator to use for scoring. Can be a built-in evaluator (e.g., <code>Builtin.Helpfulness</code>, <code>Builtin.Correctness</code>) or a custom evaluator Id created through the control plane API. </p>"""
    evaluation_input: "aws_sdk_bedrock_agentcore.types.evaluation_input.EvaluationInput"
    """<p> The input data containing agent session spans to be evaluated. Includes a list of spans in OpenTelemetry format from supported frameworks like Strands (AgentCore Runtime) or LangGraph with OpenInference instrumentation. </p>"""
    evaluation_target: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluation_target.EvaluationTarget"
    ]
    """<p> The specific trace or span IDs to evaluate within the provided input. Allows targeting evaluation at different levels: individual tool calls, single request-response interactions (traces), or entire conversation sessions. </p>"""
    evaluation_reference_inputs: NotRequired[
        "aws_sdk_bedrock_agentcore.types.evaluation_reference_inputs.EvaluationReferenceInputs"
    ]
    """<p> Ground truth data to compare against agent responses during evaluation. Allows to provide expected responses, assertions, and expected tool trajectories at different evaluation levels. Session-level reference inputs apply to the entire conversation, while trace-level reference inputs target specific request-response interactions identified by trace ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.evaluation_input

    out["evaluationInput"] = (
        aws_sdk_bedrock_agentcore.types.evaluation_input.serialize_json(
            value["evaluation_input"]
        )
    )
    if "evaluation_target" in value:
        import aws_sdk_bedrock_agentcore.types.evaluation_target

        out["evaluationTarget"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_target.serialize_json(
                value["evaluation_target"]
            )
        )
    if "evaluation_reference_inputs" in value:
        import aws_sdk_bedrock_agentcore.types.evaluation_reference_inputs

        out["evaluationReferenceInputs"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_reference_inputs.serialize_json(
                value["evaluation_reference_inputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluateRequest:
    out: EvaluateRequest = {}  # type: ignore[typeddict-item]
    if "evaluationInput" in data:
        import aws_sdk_bedrock_agentcore.types.evaluation_input

        out["evaluation_input"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_input.deserialize_json(
                data["evaluationInput"]
            )
        )
    else:
        raise DeserializationError("EvaluateRequest.evaluation_input required")
    if "evaluationTarget" in data:
        import aws_sdk_bedrock_agentcore.types.evaluation_target

        out["evaluation_target"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_target.deserialize_json(
                data["evaluationTarget"]
            )
        )
    if "evaluationReferenceInputs" in data:
        import aws_sdk_bedrock_agentcore.types.evaluation_reference_inputs

        out["evaluation_reference_inputs"] = (
            aws_sdk_bedrock_agentcore.types.evaluation_reference_inputs.deserialize_json(
                data["evaluationReferenceInputs"]
            )
        )
    return out
