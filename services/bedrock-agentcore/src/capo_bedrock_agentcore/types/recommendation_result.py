"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationResult``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.system_prompt_recommendation_result
    import capo_bedrock_agentcore.types.tool_description_recommendation_result


class _RecommendationResult_systemPromptRecommendationResult(TypedDict, closed=True):
    systemPromptRecommendationResult: "capo_bedrock_agentcore.types.system_prompt_recommendation_result.SystemPromptRecommendationResult"


class _RecommendationResult_toolDescriptionRecommendationResult(TypedDict, closed=True):
    toolDescriptionRecommendationResult: "capo_bedrock_agentcore.types.tool_description_recommendation_result.ToolDescriptionRecommendationResult"


RecommendationResult: TypeAlias = (
    _RecommendationResult_systemPromptRecommendationResult
    | _RecommendationResult_toolDescriptionRecommendationResult
)


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResult) -> dict:
    if "systemPromptRecommendationResult" in value:
        import capo_bedrock_agentcore.types.system_prompt_recommendation_result

        return {
            "systemPromptRecommendationResult": capo_bedrock_agentcore.types.system_prompt_recommendation_result.serialize_json(
                value["systemPromptRecommendationResult"]
            )
        }
    elif "toolDescriptionRecommendationResult" in value:
        import capo_bedrock_agentcore.types.tool_description_recommendation_result

        return {
            "toolDescriptionRecommendationResult": capo_bedrock_agentcore.types.tool_description_recommendation_result.serialize_json(
                value["toolDescriptionRecommendationResult"]
            )
        }
    else:
        raise SerializationError("RecommendationResult: no variant present")


def deserialize_json(data: dict) -> RecommendationResult:
    if data.get("systemPromptRecommendationResult") is not None:
        import capo_bedrock_agentcore.types.system_prompt_recommendation_result

        return {
            "systemPromptRecommendationResult": capo_bedrock_agentcore.types.system_prompt_recommendation_result.deserialize_json(
                data["systemPromptRecommendationResult"]
            )
        }
    elif data.get("toolDescriptionRecommendationResult") is not None:
        import capo_bedrock_agentcore.types.tool_description_recommendation_result

        return {
            "toolDescriptionRecommendationResult": capo_bedrock_agentcore.types.tool_description_recommendation_result.deserialize_json(
                data["toolDescriptionRecommendationResult"]
            )
        }
    else:
        raise DeserializationError("RecommendationResult: no recognized variant key")
