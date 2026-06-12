"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationPurchaseRecommendationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_detail

ReservationPurchaseRecommendationDetails: TypeAlias = list[
    "aws_sdk_cost_explorer.types.reservation_purchase_recommendation_detail.ReservationPurchaseRecommendationDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationPurchaseRecommendationDetails) -> list:
    import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.reservation_purchase_recommendation_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReservationPurchaseRecommendationDetails:
    import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_detail

    out: ReservationPurchaseRecommendationDetails = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.reservation_purchase_recommendation_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
