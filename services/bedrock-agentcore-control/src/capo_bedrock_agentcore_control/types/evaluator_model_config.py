"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorModelConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config


class _EvaluatorModelConfig_bedrockEvaluatorModelConfig(TypedDict, closed=True):
    bedrockEvaluatorModelConfig: "capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config.BedrockEvaluatorModelConfig"


EvaluatorModelConfig: TypeAlias = _EvaluatorModelConfig_bedrockEvaluatorModelConfig


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorModelConfig) -> dict:
    if "bedrockEvaluatorModelConfig" in value:
        import capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config

        return {
            "bedrockEvaluatorModelConfig": capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config.serialize_json(
                value["bedrockEvaluatorModelConfig"]
            )
        }
    else:
        raise SerializationError("EvaluatorModelConfig: no variant present")


def deserialize_json(data: dict) -> EvaluatorModelConfig:
    if data.get("bedrockEvaluatorModelConfig") is not None:
        import capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config

        return {
            "bedrockEvaluatorModelConfig": capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config.deserialize_json(
                data["bedrockEvaluatorModelConfig"]
            )
        }
    else:
        raise DeserializationError("EvaluatorModelConfig: no recognized variant key")
