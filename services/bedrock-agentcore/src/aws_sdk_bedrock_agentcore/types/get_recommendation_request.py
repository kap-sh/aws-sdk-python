"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetRecommendationRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.recommendation_id

class GetRecommendationRequest(TypedDict):
    recommendation_id: "aws_sdk_bedrock_agentcore.types.recommendation_id.RecommendationId"
    """<p>The unique identifier of the recommendation to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommendationRequest:
    out: GetRecommendationRequest = {}  # type: ignore[typeddict-item]
    return out