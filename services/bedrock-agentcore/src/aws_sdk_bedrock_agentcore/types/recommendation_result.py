"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationResult``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_result
    import aws_sdk_bedrock_agentcore.types.tool_description_recommendation_result


class _RecommendationResult_systemPromptRecommendationResult(TypedDict, closed=True):
    systemPromptRecommendationResult: "aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_result.SystemPromptRecommendationResult"


class _RecommendationResult_toolDescriptionRecommendationResult(TypedDict, closed=True):
    toolDescriptionRecommendationResult: "aws_sdk_bedrock_agentcore.types.tool_description_recommendation_result.ToolDescriptionRecommendationResult"


RecommendationResult: TypeAlias = (
    _RecommendationResult_systemPromptRecommendationResult
    | _RecommendationResult_toolDescriptionRecommendationResult
)


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResult) -> dict:
    if "systemPromptRecommendationResult" in value:
        import aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_result

        return {
            "systemPromptRecommendationResult": aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_result.serialize_json(
                value["systemPromptRecommendationResult"]
            )
        }
    elif "toolDescriptionRecommendationResult" in value:
        import aws_sdk_bedrock_agentcore.types.tool_description_recommendation_result

        return {
            "toolDescriptionRecommendationResult": aws_sdk_bedrock_agentcore.types.tool_description_recommendation_result.serialize_json(
                value["toolDescriptionRecommendationResult"]
            )
        }
    else:
        raise SerializationError("RecommendationResult: no variant present")


def deserialize_json(data: dict) -> RecommendationResult:
    if "systemPromptRecommendationResult" in data:
        import aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_result

        return {
            "systemPromptRecommendationResult": aws_sdk_bedrock_agentcore.types.system_prompt_recommendation_result.deserialize_json(
                data["systemPromptRecommendationResult"]
            )
        }
    elif "toolDescriptionRecommendationResult" in data:
        import aws_sdk_bedrock_agentcore.types.tool_description_recommendation_result

        return {
            "toolDescriptionRecommendationResult": aws_sdk_bedrock_agentcore.types.tool_description_recommendation_result.deserialize_json(
                data["toolDescriptionRecommendationResult"]
            )
        }
    else:
        raise DeserializationError("RecommendationResult: no recognized variant key")
