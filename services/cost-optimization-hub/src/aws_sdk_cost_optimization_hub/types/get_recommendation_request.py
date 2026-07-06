"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#GetRecommendationRequest``."""

from typing_extensions import TypedDict

from aws_sdk_cost_optimization_hub.errors import DeserializationError


class GetRecommendationRequest(TypedDict, closed=True):
    recommendation_id: "str"
    """<p>The ID for the recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecommendationRequest) -> dict:
    out: dict = {}
    out["recommendationId"] = value["recommendation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecommendationRequest:
    out: GetRecommendationRequest = {}  # type: ignore[typeddict-item]
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    else:
        raise DeserializationError(
            "GetRecommendationRequest.recommendation_id required"
        )
    return out
