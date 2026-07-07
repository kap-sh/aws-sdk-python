"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore.types.recommendation_arn
    import aws_sdk_bedrock_agentcore.types.recommendation_config
    import aws_sdk_bedrock_agentcore.types.recommendation_description
    import aws_sdk_bedrock_agentcore.types.recommendation_id
    import aws_sdk_bedrock_agentcore.types.recommendation_name
    import aws_sdk_bedrock_agentcore.types.recommendation_result
    import aws_sdk_bedrock_agentcore.types.recommendation_status
    import aws_sdk_bedrock_agentcore.types.recommendation_type


class GetRecommendationResponse(TypedDict, closed=True):
    recommendation_id: (
        "aws_sdk_bedrock_agentcore.types.recommendation_id.RecommendationId"
    )
    """<p>The unique identifier of the recommendation.</p>"""
    recommendation_arn: (
        "aws_sdk_bedrock_agentcore.types.recommendation_arn.RecommendationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the recommendation.</p>"""
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
    """<p>The current status of the recommendation.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the recommendation was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the recommendation was last updated.</p>"""
    recommendation_result: NotRequired[
        "aws_sdk_bedrock_agentcore.types.recommendation_result.RecommendationResult"
    ]
    """<p>The result of the recommendation, containing the optimized system prompt or tool descriptions. Only present when the recommendation status is <code>COMPLETED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationResponse) -> dict:
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
    if "recommendation_result" in value:
        import aws_sdk_bedrock_agentcore.types.recommendation_result

        out["recommendationResult"] = (
            aws_sdk_bedrock_agentcore.types.recommendation_result.serialize_json(
                value["recommendation_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRecommendationResponse:
    out: GetRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    else:
        raise DeserializationError(
            "GetRecommendationResponse.recommendation_id required"
        )
    if "recommendationArn" in data:
        out["recommendation_arn"] = data["recommendationArn"]
    else:
        raise DeserializationError(
            "GetRecommendationResponse.recommendation_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetRecommendationResponse.name required")
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
        raise DeserializationError("GetRecommendationResponse.type required")
    if "recommendationConfig" in data:
        import aws_sdk_bedrock_agentcore.types.recommendation_config

        out["recommendation_config"] = (
            aws_sdk_bedrock_agentcore.types.recommendation_config.deserialize_json(
                data["recommendationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetRecommendationResponse.recommendation_config required"
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.recommendation_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.recommendation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetRecommendationResponse.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetRecommendationResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetRecommendationResponse.updated_at required")
    if "recommendationResult" in data:
        import aws_sdk_bedrock_agentcore.types.recommendation_result

        out["recommendation_result"] = (
            aws_sdk_bedrock_agentcore.types.recommendation_result.deserialize_json(
                data["recommendationResult"]
            )
        )
    return out
