"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationPurchaseRecommendationMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class ReservationPurchaseRecommendationMetadata(TypedDict):
    recommendation_id: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The ID for the recommendation.</p>"""
    generation_timestamp: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The timestamp for when Amazon Web Services made the recommendation.</p>"""
    additional_metadata: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>Additional metadata that might be applicable to the recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationPurchaseRecommendationMetadata) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["RecommendationId"] = value["recommendation_id"]
    if "generation_timestamp" in value:
        out["GenerationTimestamp"] = value["generation_timestamp"]
    if "additional_metadata" in value:
        out["AdditionalMetadata"] = value["additional_metadata"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservationPurchaseRecommendationMetadata:
    out: ReservationPurchaseRecommendationMetadata = {}  # type: ignore[typeddict-item]
    if "RecommendationId" in data:
        out["recommendation_id"] = data["RecommendationId"]
    if "GenerationTimestamp" in data:
        out["generation_timestamp"] = data["GenerationTimestamp"]
    if "AdditionalMetadata" in data:
        out["additional_metadata"] = data["AdditionalMetadata"]
    return out
