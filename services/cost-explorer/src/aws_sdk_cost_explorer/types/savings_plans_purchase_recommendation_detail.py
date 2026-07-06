"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansPurchaseRecommendationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.recommendation_detail_id
    import aws_sdk_cost_explorer.types.savings_plans_details


class SavingsPlansPurchaseRecommendationDetail(TypedDict, closed=True):
    savings_plans_details: NotRequired[
        "aws_sdk_cost_explorer.types.savings_plans_details.SavingsPlansDetails"
    ]
    """<p>Details for your recommended Savings Plans.</p>"""
    account_id: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The <code>AccountID</code> the recommendation is generated for.</p>"""
    upfront_cost: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The upfront cost of the recommended Savings Plans, based on the selected payment option.</p>"""
    estimated_roi: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated return on investment that's based on the recommended Savings Plans that you purchased. This is calculated as <code>estimatedSavingsAmount</code>/ <code>estimatedSPCost</code>*100.</p>"""
    currency_code: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The currency code that Amazon Web Services used to generate the recommendations and present potential savings.</p>"""
    estimated_sp_cost: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The cost of the recommended Savings Plans over the length of the lookback period.</p>"""
    estimated_on_demand_cost: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The remaining On-Demand cost estimated to not be covered by the recommended Savings Plans, over the length of the lookback period.</p>"""
    estimated_on_demand_cost_with_current_commitment: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p> The estimated On-Demand costs you expect with no additional commitment, based on your usage of the selected time period and the Savings Plans you own. </p>"""
    estimated_savings_amount: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated savings amount that's based on the recommended Savings Plans over the length of the lookback period.</p>"""
    estimated_savings_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated savings percentage relative to the total cost of applicable On-Demand usage over the lookback period.</p>"""
    hourly_commitment_to_purchase: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The recommended hourly commitment level for the Savings Plans type and the configuration that's based on the usage during the lookback period.</p>"""
    estimated_average_utilization: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated utilization of the recommended Savings Plans.</p>"""
    estimated_monthly_savings_amount: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated monthly savings amount based on the recommended Savings Plans.</p>"""
    current_minimum_hourly_on_demand_spend: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The lowest value of hourly On-Demand spend over the lookback period of the applicable usage type.</p>"""
    current_maximum_hourly_on_demand_spend: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The highest value of hourly On-Demand spend over the lookback period of the applicable usage type.</p>"""
    current_average_hourly_on_demand_spend: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The average value of hourly On-Demand spend over the lookback period of the applicable usage type.</p>"""
    recommendation_detail_id: NotRequired[
        "aws_sdk_cost_explorer.types.recommendation_detail_id.RecommendationDetailId"
    ]
    """<p>Contains detailed information about a specific Savings Plan recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansPurchaseRecommendationDetail) -> dict:
    out: dict = {}
    if "savings_plans_details" in value:
        import aws_sdk_cost_explorer.types.savings_plans_details

        out["SavingsPlansDetails"] = (
            aws_sdk_cost_explorer.types.savings_plans_details.serialize_aws_json_1_1(
                value["savings_plans_details"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "upfront_cost" in value:
        out["UpfrontCost"] = value["upfront_cost"]
    if "estimated_roi" in value:
        out["EstimatedROI"] = value["estimated_roi"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    if "estimated_sp_cost" in value:
        out["EstimatedSPCost"] = value["estimated_sp_cost"]
    if "estimated_on_demand_cost" in value:
        out["EstimatedOnDemandCost"] = value["estimated_on_demand_cost"]
    if "estimated_on_demand_cost_with_current_commitment" in value:
        out["EstimatedOnDemandCostWithCurrentCommitment"] = value[
            "estimated_on_demand_cost_with_current_commitment"
        ]
    if "estimated_savings_amount" in value:
        out["EstimatedSavingsAmount"] = value["estimated_savings_amount"]
    if "estimated_savings_percentage" in value:
        out["EstimatedSavingsPercentage"] = value["estimated_savings_percentage"]
    if "hourly_commitment_to_purchase" in value:
        out["HourlyCommitmentToPurchase"] = value["hourly_commitment_to_purchase"]
    if "estimated_average_utilization" in value:
        out["EstimatedAverageUtilization"] = value["estimated_average_utilization"]
    if "estimated_monthly_savings_amount" in value:
        out["EstimatedMonthlySavingsAmount"] = value["estimated_monthly_savings_amount"]
    if "current_minimum_hourly_on_demand_spend" in value:
        out["CurrentMinimumHourlyOnDemandSpend"] = value[
            "current_minimum_hourly_on_demand_spend"
        ]
    if "current_maximum_hourly_on_demand_spend" in value:
        out["CurrentMaximumHourlyOnDemandSpend"] = value[
            "current_maximum_hourly_on_demand_spend"
        ]
    if "current_average_hourly_on_demand_spend" in value:
        out["CurrentAverageHourlyOnDemandSpend"] = value[
            "current_average_hourly_on_demand_spend"
        ]
    if "recommendation_detail_id" in value:
        out["RecommendationDetailId"] = value["recommendation_detail_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansPurchaseRecommendationDetail:
    out: SavingsPlansPurchaseRecommendationDetail = {}  # type: ignore[typeddict-item]
    if "SavingsPlansDetails" in data:
        import aws_sdk_cost_explorer.types.savings_plans_details

        out["savings_plans_details"] = (
            aws_sdk_cost_explorer.types.savings_plans_details.deserialize_aws_json_1_1(
                data["SavingsPlansDetails"]
            )
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "UpfrontCost" in data:
        out["upfront_cost"] = data["UpfrontCost"]
    if "EstimatedROI" in data:
        out["estimated_roi"] = data["EstimatedROI"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "EstimatedSPCost" in data:
        out["estimated_sp_cost"] = data["EstimatedSPCost"]
    if "EstimatedOnDemandCost" in data:
        out["estimated_on_demand_cost"] = data["EstimatedOnDemandCost"]
    if "EstimatedOnDemandCostWithCurrentCommitment" in data:
        out["estimated_on_demand_cost_with_current_commitment"] = data[
            "EstimatedOnDemandCostWithCurrentCommitment"
        ]
    if "EstimatedSavingsAmount" in data:
        out["estimated_savings_amount"] = data["EstimatedSavingsAmount"]
    if "EstimatedSavingsPercentage" in data:
        out["estimated_savings_percentage"] = data["EstimatedSavingsPercentage"]
    if "HourlyCommitmentToPurchase" in data:
        out["hourly_commitment_to_purchase"] = data["HourlyCommitmentToPurchase"]
    if "EstimatedAverageUtilization" in data:
        out["estimated_average_utilization"] = data["EstimatedAverageUtilization"]
    if "EstimatedMonthlySavingsAmount" in data:
        out["estimated_monthly_savings_amount"] = data["EstimatedMonthlySavingsAmount"]
    if "CurrentMinimumHourlyOnDemandSpend" in data:
        out["current_minimum_hourly_on_demand_spend"] = data[
            "CurrentMinimumHourlyOnDemandSpend"
        ]
    if "CurrentMaximumHourlyOnDemandSpend" in data:
        out["current_maximum_hourly_on_demand_spend"] = data[
            "CurrentMaximumHourlyOnDemandSpend"
        ]
    if "CurrentAverageHourlyOnDemandSpend" in data:
        out["current_average_hourly_on_demand_spend"] = data[
            "CurrentAverageHourlyOnDemandSpend"
        ]
    if "RecommendationDetailId" in data:
        out["recommendation_detail_id"] = data["RecommendationDetailId"]
    return out
