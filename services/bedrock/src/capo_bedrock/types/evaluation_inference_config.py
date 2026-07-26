"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationInferenceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_model_configs
    import capo_bedrock.types.rag_configs


class _EvaluationInferenceConfig_models(TypedDict, closed=True):
    models: "capo_bedrock.types.evaluation_model_configs.EvaluationModelConfigs"


class _EvaluationInferenceConfig_ragConfigs(TypedDict, closed=True):
    ragConfigs: "capo_bedrock.types.rag_configs.RagConfigs"


EvaluationInferenceConfig: TypeAlias = (
    _EvaluationInferenceConfig_models | _EvaluationInferenceConfig_ragConfigs
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationInferenceConfig) -> dict:
    if "models" in value:
        import capo_bedrock.types.evaluation_model_configs

        return {
            "models": capo_bedrock.types.evaluation_model_configs.serialize_json(
                value["models"]
            )
        }
    elif "ragConfigs" in value:
        import capo_bedrock.types.rag_configs

        return {
            "ragConfigs": capo_bedrock.types.rag_configs.serialize_json(
                value["ragConfigs"]
            )
        }
    else:
        raise SerializationError("EvaluationInferenceConfig: no variant present")


def deserialize_json(data: dict) -> EvaluationInferenceConfig:
    if "models" in data:
        import capo_bedrock.types.evaluation_model_configs

        return {
            "models": capo_bedrock.types.evaluation_model_configs.deserialize_json(
                data["models"]
            )
        }
    elif "ragConfigs" in data:
        import capo_bedrock.types.rag_configs

        return {
            "ragConfigs": capo_bedrock.types.rag_configs.deserialize_json(
                data["ragConfigs"]
            )
        }
    else:
        raise DeserializationError(
            "EvaluationInferenceConfig: no recognized variant key"
        )
