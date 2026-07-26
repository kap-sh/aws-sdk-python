"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationPurchaseRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.reservation_purchase_recommendation

ReservationPurchaseRecommendations: TypeAlias = list[
    "capo_cost_explorer.types.reservation_purchase_recommendation.ReservationPurchaseRecommendation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationPurchaseRecommendations) -> list:
    import capo_cost_explorer.types.reservation_purchase_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.reservation_purchase_recommendation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReservationPurchaseRecommendations:
    import capo_cost_explorer.types.reservation_purchase_recommendation

    out: ReservationPurchaseRecommendations = []
    for item in data:
        out.append(
            capo_cost_explorer.types.reservation_purchase_recommendation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
