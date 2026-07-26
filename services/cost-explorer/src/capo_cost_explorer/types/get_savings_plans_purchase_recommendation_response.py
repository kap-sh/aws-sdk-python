"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlansPurchaseRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.savings_plans_purchase_recommendation
    import capo_cost_explorer.types.savings_plans_purchase_recommendation_metadata


class GetSavingsPlansPurchaseRecommendationResponse(TypedDict, closed=True):
    metadata: NotRequired[
        "capo_cost_explorer.types.savings_plans_purchase_recommendation_metadata.SavingsPlansPurchaseRecommendationMetadata"
    ]
    """<p>Information that regards this specific recommendation set.</p>"""
    savings_plans_purchase_recommendation: NotRequired[
        "capo_cost_explorer.types.savings_plans_purchase_recommendation.SavingsPlansPurchaseRecommendation"
    ]
    """<p>Contains your request parameters, Savings Plan Recommendations Summary, and Details.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token for the next set of retrievable results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetSavingsPlansPurchaseRecommendationResponse,
) -> dict:
    out: dict = {}
    if "metadata" in value:
        import capo_cost_explorer.types.savings_plans_purchase_recommendation_metadata

        out["Metadata"] = (
            capo_cost_explorer.types.savings_plans_purchase_recommendation_metadata.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    if "savings_plans_purchase_recommendation" in value:
        import capo_cost_explorer.types.savings_plans_purchase_recommendation

        out["SavingsPlansPurchaseRecommendation"] = (
            capo_cost_explorer.types.savings_plans_purchase_recommendation.serialize_aws_json_1_1(
                value["savings_plans_purchase_recommendation"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetSavingsPlansPurchaseRecommendationResponse:
    out: GetSavingsPlansPurchaseRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "Metadata" in data:
        import capo_cost_explorer.types.savings_plans_purchase_recommendation_metadata

        out["metadata"] = (
            capo_cost_explorer.types.savings_plans_purchase_recommendation_metadata.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    if "SavingsPlansPurchaseRecommendation" in data:
        import capo_cost_explorer.types.savings_plans_purchase_recommendation

        out["savings_plans_purchase_recommendation"] = (
            capo_cost_explorer.types.savings_plans_purchase_recommendation.deserialize_aws_json_1_1(
                data["SavingsPlansPurchaseRecommendation"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
