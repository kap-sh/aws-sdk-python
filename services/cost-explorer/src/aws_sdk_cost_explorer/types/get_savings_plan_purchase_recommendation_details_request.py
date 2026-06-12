"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlanPurchaseRecommendationDetailsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.recommendation_detail_id


class GetSavingsPlanPurchaseRecommendationDetailsRequest(TypedDict):
    recommendation_detail_id: (
        "aws_sdk_cost_explorer.types.recommendation_detail_id.RecommendationDetailId"
    )
    """<p>The ID that is associated with the Savings Plan recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetSavingsPlanPurchaseRecommendationDetailsRequest,
) -> dict:
    out: dict = {}
    out["RecommendationDetailId"] = value["recommendation_detail_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetSavingsPlanPurchaseRecommendationDetailsRequest:
    out: GetSavingsPlanPurchaseRecommendationDetailsRequest = {}  # type: ignore[typeddict-item]
    if "RecommendationDetailId" in data:
        out["recommendation_detail_id"] = data["RecommendationDetailId"]
    else:
        raise DeserializationError(
            "GetSavingsPlanPurchaseRecommendationDetailsRequest.recommendation_detail_id required"
        )
    return out
