"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.recommendation_config
    import aws_sdk_bedrock_agentcore.types.recommendation_description
    import aws_sdk_bedrock_agentcore.types.recommendation_name
    import aws_sdk_bedrock_agentcore.types.recommendation_type


class StartRecommendationRequest(TypedDict, closed=True):
    name: "aws_sdk_bedrock_agentcore.types.recommendation_name.RecommendationName"
    """<p>The name of the recommendation. Must be unique within your account.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore.types.recommendation_description.RecommendationDescription"
    ]
    """<p>The description of the recommendation.</p>"""
    type: "aws_sdk_bedrock_agentcore.types.recommendation_type.RecommendationType"
    """<p>The type of recommendation to generate. Valid values are <code>SYSTEM_PROMPT_RECOMMENDATION</code> for system prompt optimization or <code>TOOL_DESCRIPTION_RECOMMENDATION</code> for tool description optimization.</p>"""
    recommendation_config: (
        "aws_sdk_bedrock_agentcore.types.recommendation_config.RecommendationConfig"
    )
    """<p>The configuration for the recommendation, including the input to optimize, agent traces to analyze, and evaluation settings.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRecommendationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore.types.recommendation_type

    out["type"] = aws_sdk_bedrock_agentcore.types.recommendation_type.serialize_json(
        value["type"]
    )
    import aws_sdk_bedrock_agentcore.types.recommendation_config

    out["recommendationConfig"] = (
        aws_sdk_bedrock_agentcore.types.recommendation_config.serialize_json(
            value["recommendation_config"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartRecommendationRequest:
    out: StartRecommendationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StartRecommendationRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import aws_sdk_bedrock_agentcore.types.recommendation_type

        out["type"] = (
            aws_sdk_bedrock_agentcore.types.recommendation_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("StartRecommendationRequest.type required")
    if "recommendationConfig" in data:
        import aws_sdk_bedrock_agentcore.types.recommendation_config

        out["recommendation_config"] = (
            aws_sdk_bedrock_agentcore.types.recommendation_config.deserialize_json(
                data["recommendationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartRecommendationRequest.recommendation_config required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
