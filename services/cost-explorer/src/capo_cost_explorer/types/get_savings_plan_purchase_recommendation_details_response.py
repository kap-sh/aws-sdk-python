"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlanPurchaseRecommendationDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.recommendation_detail_data
    import capo_cost_explorer.types.recommendation_detail_id


class GetSavingsPlanPurchaseRecommendationDetailsResponse(TypedDict, closed=True):
    recommendation_detail_id: NotRequired[
        "capo_cost_explorer.types.recommendation_detail_id.RecommendationDetailId"
    ]
    """<p>The ID that is associated with the Savings Plan recommendation.</p>"""
    recommendation_detail_data: NotRequired[
        "capo_cost_explorer.types.recommendation_detail_data.RecommendationDetailData"
    ]
    """<p>Contains detailed information about a specific Savings Plan recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetSavingsPlanPurchaseRecommendationDetailsResponse,
) -> dict:
    out: dict = {}
    if "recommendation_detail_id" in value:
        out["RecommendationDetailId"] = value["recommendation_detail_id"]
    if "recommendation_detail_data" in value:
        import capo_cost_explorer.types.recommendation_detail_data

        out["RecommendationDetailData"] = (
            capo_cost_explorer.types.recommendation_detail_data.serialize_aws_json_1_1(
                value["recommendation_detail_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetSavingsPlanPurchaseRecommendationDetailsResponse:
    out: GetSavingsPlanPurchaseRecommendationDetailsResponse = {}  # type: ignore[typeddict-item]
    if "RecommendationDetailId" in data:
        out["recommendation_detail_id"] = data["RecommendationDetailId"]
    if "RecommendationDetailData" in data:
        import capo_cost_explorer.types.recommendation_detail_data

        out["recommendation_detail_data"] = (
            capo_cost_explorer.types.recommendation_detail_data.deserialize_aws_json_1_1(
                data["RecommendationDetailData"]
            )
        )
    return out
