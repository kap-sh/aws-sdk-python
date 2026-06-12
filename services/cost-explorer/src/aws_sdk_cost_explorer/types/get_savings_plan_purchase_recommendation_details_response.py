"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlanPurchaseRecommendationDetailsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.recommendation_detail_data
    import aws_sdk_cost_explorer.types.recommendation_detail_id


class GetSavingsPlanPurchaseRecommendationDetailsResponse(TypedDict):
    recommendation_detail_id: NotRequired[
        "aws_sdk_cost_explorer.types.recommendation_detail_id.RecommendationDetailId"
    ]
    """<p>The ID that is associated with the Savings Plan recommendation.</p>"""
    recommendation_detail_data: NotRequired[
        "aws_sdk_cost_explorer.types.recommendation_detail_data.RecommendationDetailData"
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
        import aws_sdk_cost_explorer.types.recommendation_detail_data

        out["RecommendationDetailData"] = (
            aws_sdk_cost_explorer.types.recommendation_detail_data.serialize_aws_json_1_1(
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
        import aws_sdk_cost_explorer.types.recommendation_detail_data

        out["recommendation_detail_data"] = (
            aws_sdk_cost_explorer.types.recommendation_detail_data.deserialize_aws_json_1_1(
                data["RecommendationDetailData"]
            )
        )
    return out
