"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteRecommendationRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.recommendation_id

class DeleteRecommendationRequest(TypedDict):
    recommendation_id: "aws_sdk_bedrock_agentcore.types.recommendation_id.RecommendationId"
    """<p>The unique identifier of the recommendation to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommendationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRecommendationRequest:
    out: DeleteRecommendationRequest = {}  # type: ignore[typeddict-item]
    return out