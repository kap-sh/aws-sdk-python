"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LlmAsAJudgeEvaluatorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.evaluator_instructions
    import aws_sdk_bedrock_agentcore_control.types.evaluator_model_config
    import aws_sdk_bedrock_agentcore_control.types.rating_scale


class LlmAsAJudgeEvaluatorConfig(TypedDict, closed=True):
    instructions: "aws_sdk_bedrock_agentcore_control.types.evaluator_instructions.EvaluatorInstructions"
    """<p> The evaluation instructions that guide the language model in assessing agent performance, including criteria and evaluation guidelines. </p>"""
    rating_scale: "aws_sdk_bedrock_agentcore_control.types.rating_scale.RatingScale"
    """<p> The rating scale that defines how the evaluator should score agent performance, either numerical or categorical. </p>"""
    model_config: "aws_sdk_bedrock_agentcore_control.types.evaluator_model_config.EvaluatorModelConfig"
    """<p> The model configuration that specifies which foundation model to use and how to configure it for evaluation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LlmAsAJudgeEvaluatorConfig) -> dict:
    out: dict = {}
    out["instructions"] = value["instructions"]
    import aws_sdk_bedrock_agentcore_control.types.rating_scale

    out["ratingScale"] = (
        aws_sdk_bedrock_agentcore_control.types.rating_scale.serialize_json(
            value["rating_scale"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.evaluator_model_config

    out["modelConfig"] = (
        aws_sdk_bedrock_agentcore_control.types.evaluator_model_config.serialize_json(
            value["model_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> LlmAsAJudgeEvaluatorConfig:
    out: LlmAsAJudgeEvaluatorConfig = {}  # type: ignore[typeddict-item]
    if "instructions" in data:
        out["instructions"] = data["instructions"]
    else:
        raise DeserializationError("LlmAsAJudgeEvaluatorConfig.instructions required")
    if "ratingScale" in data:
        import aws_sdk_bedrock_agentcore_control.types.rating_scale

        out["rating_scale"] = (
            aws_sdk_bedrock_agentcore_control.types.rating_scale.deserialize_json(
                data["ratingScale"]
            )
        )
    else:
        raise DeserializationError("LlmAsAJudgeEvaluatorConfig.rating_scale required")
    if "modelConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.evaluator_model_config

        out["model_config"] = (
            aws_sdk_bedrock_agentcore_control.types.evaluator_model_config.deserialize_json(
                data["modelConfig"]
            )
        )
    else:
        raise DeserializationError("LlmAsAJudgeEvaluatorConfig.model_config required")
    return out
