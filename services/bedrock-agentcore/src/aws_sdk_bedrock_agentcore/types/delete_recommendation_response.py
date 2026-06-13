"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteRecommendationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.recommendation_id
    import aws_sdk_bedrock_agentcore.types.recommendation_status

class DeleteRecommendationResponse(TypedDict):
    recommendation_id: "aws_sdk_bedrock_agentcore.types.recommendation_id.RecommendationId"
    """<p>The unique identifier of the deleted recommendation.</p>"""
    status: "aws_sdk_bedrock_agentcore.types.recommendation_status.RecommendationStatus"
    """<p>The status of the recommendation deletion operation.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommendationResponse) -> dict:
    out: dict = {}
    out["recommendationId"] = value["recommendation_id"]
    import aws_sdk_bedrock_agentcore.types.recommendation_status
    out["status"] = aws_sdk_bedrock_agentcore.types.recommendation_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteRecommendationResponse:
    out: DeleteRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    else:
        raise DeserializationError("DeleteRecommendationResponse.recommendation_id required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.recommendation_status
        out["status"] = aws_sdk_bedrock_agentcore.types.recommendation_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("DeleteRecommendationResponse.status required")
    return out