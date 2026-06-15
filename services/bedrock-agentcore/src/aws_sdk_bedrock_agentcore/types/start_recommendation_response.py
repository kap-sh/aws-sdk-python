"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StartRecommendationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore.types.recommendation_arn
    import aws_sdk_bedrock_agentcore.types.recommendation_config
    import aws_sdk_bedrock_agentcore.types.recommendation_description
    import aws_sdk_bedrock_agentcore.types.recommendation_id
    import aws_sdk_bedrock_agentcore.types.recommendation_name
    import aws_sdk_bedrock_agentcore.types.recommendation_status
    import aws_sdk_bedrock_agentcore.types.recommendation_type


class StartRecommendationResponse(TypedDict):
    recommendation_id: (
        "aws_sdk_bedrock_agentcore.types.recommendation_id.RecommendationId"
    )
    """<p>The unique identifier of the created recommendation.</p>"""
    recommendation_arn: (
        "aws_sdk_bedrock_agentcore.types.recommendation_arn.RecommendationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the created recommendation.</p>"""
    name: "aws_sdk_bedrock_agentcore.types.recommendation_name.RecommendationName"
    """<p>The name of the recommendation.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore.types.recommendation_description.RecommendationDescription"
    ]
    """<p>The description of the recommendation.</p>"""
    type: "aws_sdk_bedrock_agentcore.types.recommendation_type.RecommendationType"
    """<p>The type of recommendation.</p>"""
    recommendation_config: (
        "aws_sdk_bedrock_agentcore.types.recommendation_config.RecommendationConfig"
    )
    """<p>The configuration for the recommendation.</p>"""
    status: "aws_sdk_bedrock_agentcore.types.recommendation_status.RecommendationStatus"
    """<p>The status of the recommendation.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the recommendation was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the recommendation was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRecommendationResponse) -> dict:
    out: dict = {}
    out["recommendationId"] = value["recommendation_id"]
    out["recommendationArn"] = value["recommendation_arn"]
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
    import aws_sdk_bedrock_agentcore.types.recommendation_status

    out["status"] = (
        aws_sdk_bedrock_agentcore.types.recommendation_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore.types._prelude.timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore.types._prelude.timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartRecommendationResponse:
    out: StartRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    else:
        raise DeserializationError(
            "StartRecommendationResponse.recommendation_id required"
        )
    if "recommendationArn" in data:
        out["recommendation_arn"] = data["recommendationArn"]
    else:
        raise DeserializationError(
            "StartRecommendationResponse.recommendation_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StartRecommendationResponse.name required")
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
        raise DeserializationError("StartRecommendationResponse.type required")
    if "recommendationConfig" in data:
        import aws_sdk_bedrock_agentcore.types.recommendation_config

        out["recommendation_config"] = (
            aws_sdk_bedrock_agentcore.types.recommendation_config.deserialize_json(
                data["recommendationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartRecommendationResponse.recommendation_config required"
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.recommendation_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.recommendation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("StartRecommendationResponse.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("StartRecommendationResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("StartRecommendationResponse.updated_at required")
    return out
