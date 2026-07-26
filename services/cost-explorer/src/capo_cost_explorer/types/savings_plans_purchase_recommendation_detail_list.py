"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansPurchaseRecommendationDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.savings_plans_purchase_recommendation_detail

SavingsPlansPurchaseRecommendationDetailList: TypeAlias = list[
    "capo_cost_explorer.types.savings_plans_purchase_recommendation_detail.SavingsPlansPurchaseRecommendationDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansPurchaseRecommendationDetailList) -> list:
    import capo_cost_explorer.types.savings_plans_purchase_recommendation_detail

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.savings_plans_purchase_recommendation_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> SavingsPlansPurchaseRecommendationDetailList:
    import capo_cost_explorer.types.savings_plans_purchase_recommendation_detail

    out: SavingsPlansPurchaseRecommendationDetailList = []
    for item in data:
        out.append(
            capo_cost_explorer.types.savings_plans_purchase_recommendation_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
