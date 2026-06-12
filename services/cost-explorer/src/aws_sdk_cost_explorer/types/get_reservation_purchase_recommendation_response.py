"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetReservationPurchaseRecommendationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_metadata
    import aws_sdk_cost_explorer.types.reservation_purchase_recommendations


class GetReservationPurchaseRecommendationResponse(TypedDict):
    metadata: NotRequired[
        "aws_sdk_cost_explorer.types.reservation_purchase_recommendation_metadata.ReservationPurchaseRecommendationMetadata"
    ]
    """<p>Information about this specific recommendation call, such as the time stamp for when Cost Explorer generated this recommendation.</p>"""
    recommendations: NotRequired[
        "aws_sdk_cost_explorer.types.reservation_purchase_recommendations.ReservationPurchaseRecommendations"
    ]
    """<p>Recommendations for reservations to purchase.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The pagination token for the next set of retrievable results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReservationPurchaseRecommendationResponse) -> dict:
    out: dict = {}
    if "metadata" in value:
        import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_metadata

        out["Metadata"] = (
            aws_sdk_cost_explorer.types.reservation_purchase_recommendation_metadata.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    if "recommendations" in value:
        import aws_sdk_cost_explorer.types.reservation_purchase_recommendations

        out["Recommendations"] = (
            aws_sdk_cost_explorer.types.reservation_purchase_recommendations.serialize_aws_json_1_1(
                value["recommendations"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetReservationPurchaseRecommendationResponse:
    out: GetReservationPurchaseRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "Metadata" in data:
        import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_metadata

        out["metadata"] = (
            aws_sdk_cost_explorer.types.reservation_purchase_recommendation_metadata.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    if "Recommendations" in data:
        import aws_sdk_cost_explorer.types.reservation_purchase_recommendations

        out["recommendations"] = (
            aws_sdk_cost_explorer.types.reservation_purchase_recommendations.deserialize_aws_json_1_1(
                data["Recommendations"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
