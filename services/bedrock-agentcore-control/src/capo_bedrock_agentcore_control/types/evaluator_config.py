"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.code_based_evaluator_config
    import capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config


class _EvaluatorConfig_llmAsAJudge(TypedDict, closed=True):
    llmAsAJudge: "capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config.LlmAsAJudgeEvaluatorConfig"


class _EvaluatorConfig_codeBased(TypedDict, closed=True):
    codeBased: "capo_bedrock_agentcore_control.types.code_based_evaluator_config.CodeBasedEvaluatorConfig"


EvaluatorConfig: TypeAlias = _EvaluatorConfig_llmAsAJudge | _EvaluatorConfig_codeBased


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorConfig) -> dict:
    if "llmAsAJudge" in value:
        import capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config

        return {
            "llmAsAJudge": capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config.serialize_json(
                value["llmAsAJudge"]
            )
        }
    elif "codeBased" in value:
        import capo_bedrock_agentcore_control.types.code_based_evaluator_config

        return {
            "codeBased": capo_bedrock_agentcore_control.types.code_based_evaluator_config.serialize_json(
                value["codeBased"]
            )
        }
    else:
        raise SerializationError("EvaluatorConfig: no variant present")


def deserialize_json(data: dict) -> EvaluatorConfig:
    if data.get("llmAsAJudge") is not None:
        import capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config

        return {
            "llmAsAJudge": capo_bedrock_agentcore_control.types.llm_as_a_judge_evaluator_config.deserialize_json(
                data["llmAsAJudge"]
            )
        }
    elif data.get("codeBased") is not None:
        import capo_bedrock_agentcore_control.types.code_based_evaluator_config

        return {
            "codeBased": capo_bedrock_agentcore_control.types.code_based_evaluator_config.deserialize_json(
                data["codeBased"]
            )
        }
    else:
        raise DeserializationError("EvaluatorConfig: no recognized variant key")
