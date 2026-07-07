"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_config
    import aws_sdk_bedrock_agentcore.types.tool_description_recommendation_config


class _RecommendationConfig_systemPromptRecommendationConfig(TypedDict, closed=True):
    systemPromptRecommendationConfig: "aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_config.SystemPromptRecommendationConfig"


class _RecommendationConfig_toolDescriptionRecommendationConfig(TypedDict, closed=True):
    toolDescriptionRecommendationConfig: "aws_sdk_bedrock_agentcore.types.tool_description_recommendation_config.ToolDescriptionRecommendationConfig"


RecommendationConfig: TypeAlias = (
    _RecommendationConfig_systemPromptRecommendationConfig
    | _RecommendationConfig_toolDescriptionRecommendationConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationConfig) -> dict:
    if "systemPromptRecommendationConfig" in value:
        import aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_config

        return {
            "systemPromptRecommendationConfig": aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_config.serialize_json(
                value["systemPromptRecommendationConfig"]
            )
        }
    elif "toolDescriptionRecommendationConfig" in value:
        import aws_sdk_bedrock_agentcore.types.tool_description_recommendation_config

        return {
            "toolDescriptionRecommendationConfig": aws_sdk_bedrock_agentcore.types.tool_description_recommendation_config.serialize_json(
                value["toolDescriptionRecommendationConfig"]
            )
        }
    else:
        raise SerializationError("RecommendationConfig: no variant present")


def deserialize_json(data: dict) -> RecommendationConfig:
    if "systemPromptRecommendationConfig" in data:
        import aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_config

        return {
            "systemPromptRecommendationConfig": aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_config.deserialize_json(
                data["systemPromptRecommendationConfig"]
            )
        }
    elif "toolDescriptionRecommendationConfig" in data:
        import aws_sdk_bedrock_agentcore.types.tool_description_recommendation_config

        return {
            "toolDescriptionRecommendationConfig": aws_sdk_bedrock_agentcore.types.tool_description_recommendation_config.deserialize_json(
                data["toolDescriptionRecommendationConfig"]
            )
        }
    else:
        raise DeserializationError("RecommendationConfig: no recognized variant key")
