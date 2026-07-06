"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansPurchaseRecommendationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class SavingsPlansPurchaseRecommendationSummary(TypedDict, closed=True):
    estimated_roi: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated return on investment that's based on the recommended Savings Plans and estimated savings.</p>"""
    currency_code: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The currency code that Amazon Web Services used to generate the recommendations and present potential savings.</p>"""
    estimated_total_cost: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated total cost of the usage after purchasing the recommended Savings Plans. This is a sum of the cost of Savings Plans during this term, and the remaining On-Demand usage.</p>"""
    current_on_demand_spend: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The current total on demand spend of the applicable usage types over the lookback period.</p>"""
    estimated_savings_amount: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated total savings over the lookback period, based on the purchase of the recommended Savings Plans.</p>"""
    total_recommendation_count: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The aggregate number of Savings Plans recommendations that exist for your account.</p>"""
    daily_commitment_to_purchase: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The recommended Savings Plans cost on a daily (24 hourly) basis.</p>"""
    hourly_commitment_to_purchase: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The recommended hourly commitment that's based on the recommendation parameters.</p>"""
    estimated_savings_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated savings relative to the total cost of On-Demand usage, over the lookback period. This is calculated as <code>estimatedSavingsAmount</code>/ <code>CurrentOnDemandSpend</code>*100.</p>"""
    estimated_monthly_savings_amount: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated monthly savings amount that's based on the recommended Savings Plans purchase.</p>"""
    estimated_on_demand_cost_with_current_commitment: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated On-Demand costs you expect with no additional commitment. It's based on your usage of the selected time period and the Savings Plans you own. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansPurchaseRecommendationSummary) -> dict:
    out: dict = {}
    if "estimated_roi" in value:
        out["EstimatedROI"] = value["estimated_roi"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    if "estimated_total_cost" in value:
        out["EstimatedTotalCost"] = value["estimated_total_cost"]
    if "current_on_demand_spend" in value:
        out["CurrentOnDemandSpend"] = value["current_on_demand_spend"]
    if "estimated_savings_amount" in value:
        out["EstimatedSavingsAmount"] = value["estimated_savings_amount"]
    if "total_recommendation_count" in value:
        out["TotalRecommendationCount"] = value["total_recommendation_count"]
    if "daily_commitment_to_purchase" in value:
        out["DailyCommitmentToPurchase"] = value["daily_commitment_to_purchase"]
    if "hourly_commitment_to_purchase" in value:
        out["HourlyCommitmentToPurchase"] = value["hourly_commitment_to_purchase"]
    if "estimated_savings_percentage" in value:
        out["EstimatedSavingsPercentage"] = value["estimated_savings_percentage"]
    if "estimated_monthly_savings_amount" in value:
        out["EstimatedMonthlySavingsAmount"] = value["estimated_monthly_savings_amount"]
    if "estimated_on_demand_cost_with_current_commitment" in value:
        out["EstimatedOnDemandCostWithCurrentCommitment"] = value[
            "estimated_on_demand_cost_with_current_commitment"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansPurchaseRecommendationSummary:
    out: SavingsPlansPurchaseRecommendationSummary = {}  # type: ignore[typeddict-item]
    if "EstimatedROI" in data:
        out["estimated_roi"] = data["EstimatedROI"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "EstimatedTotalCost" in data:
        out["estimated_total_cost"] = data["EstimatedTotalCost"]
    if "CurrentOnDemandSpend" in data:
        out["current_on_demand_spend"] = data["CurrentOnDemandSpend"]
    if "EstimatedSavingsAmount" in data:
        out["estimated_savings_amount"] = data["EstimatedSavingsAmount"]
    if "TotalRecommendationCount" in data:
        out["total_recommendation_count"] = data["TotalRecommendationCount"]
    if "DailyCommitmentToPurchase" in data:
        out["daily_commitment_to_purchase"] = data["DailyCommitmentToPurchase"]
    if "HourlyCommitmentToPurchase" in data:
        out["hourly_commitment_to_purchase"] = data["HourlyCommitmentToPurchase"]
    if "EstimatedSavingsPercentage" in data:
        out["estimated_savings_percentage"] = data["EstimatedSavingsPercentage"]
    if "EstimatedMonthlySavingsAmount" in data:
        out["estimated_monthly_savings_amount"] = data["EstimatedMonthlySavingsAmount"]
    if "EstimatedOnDemandCostWithCurrentCommitment" in data:
        out["estimated_on_demand_cost_with_current_commitment"] = data[
            "EstimatedOnDemandCostWithCurrentCommitment"
        ]
    return out
