"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansPurchaseAnalysisDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.metrics_over_lookback_period


class SavingsPlansPurchaseAnalysisDetails(TypedDict, closed=True):
    currency_code: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The currency code used for the analysis.</p>"""
    lookback_period_in_hours: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The lookback period in hours that's used to generate the analysis.</p>"""
    current_average_coverage: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The average value of hourly coverage over the lookback period.</p>"""
    current_average_hourly_on_demand_spend: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The average value of hourly On-Demand spend over the lookback period.</p>"""
    current_maximum_hourly_on_demand_spend: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The highest value of hourly On-Demand spend over the lookback period.</p>"""
    current_minimum_hourly_on_demand_spend: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The lowest value of hourly On-Demand spend over the lookback period.</p>"""
    current_on_demand_spend: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The current total On-Demand spend over the lookback period.</p>"""
    existing_hourly_commitment: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The existing hourly commitment for the Savings Plan type.</p>"""
    hourly_commitment_to_purchase: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The recommended or custom hourly commitment.</p>"""
    estimated_average_coverage: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated coverage of the Savings Plan.</p>"""
    estimated_average_utilization: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated utilization of the Savings Plan.</p>"""
    estimated_monthly_savings_amount: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated monthly savings amount based on the Savings Plan.</p>"""
    estimated_on_demand_cost: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The remaining On-Demand cost estimated to not be covered by the Savings Plan over the length of the lookback period.</p>"""
    estimated_on_demand_cost_with_current_commitment: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated On-Demand cost you expect with no additional commitment based on your usage of the selected time period and the Savings Plan you own.</p>"""
    estimated_roi: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The estimated return on investment that's based on the Savings Plan and estimated savings. This is calculated as estimatedSavingsAmount/estimatedSPCost*100.</p>"""
    estimated_savings_amount: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated savings amount that's based on the Savings Plan over the length of the lookback period.</p>"""
    estimated_savings_percentage: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated savings percentage relative to the total cost over the cost calculation lookback period.</p>"""
    estimated_commitment_cost: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated cost of the Savings Plan over the length of the lookback period.</p>"""
    latest_usage_timestamp: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The date and time of the last hour that went into the analysis.</p>"""
    upfront_cost: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The upfront cost of the Savings Plan based on the selected payment option.</p>"""
    additional_metadata: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>Additional metadata that might be applicable to the commitment.</p>"""
    metrics_over_lookback_period: NotRequired[
        "capo_cost_explorer.types.metrics_over_lookback_period.MetricsOverLookbackPeriod"
    ]
    """<p>The related hourly cost, coverage, and utilization metrics over the lookback period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansPurchaseAnalysisDetails) -> dict:
    out: dict = {}
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    if "lookback_period_in_hours" in value:
        out["LookbackPeriodInHours"] = value["lookback_period_in_hours"]
    if "current_average_coverage" in value:
        out["CurrentAverageCoverage"] = value["current_average_coverage"]
    if "current_average_hourly_on_demand_spend" in value:
        out["CurrentAverageHourlyOnDemandSpend"] = value[
            "current_average_hourly_on_demand_spend"
        ]
    if "current_maximum_hourly_on_demand_spend" in value:
        out["CurrentMaximumHourlyOnDemandSpend"] = value[
            "current_maximum_hourly_on_demand_spend"
        ]
    if "current_minimum_hourly_on_demand_spend" in value:
        out["CurrentMinimumHourlyOnDemandSpend"] = value[
            "current_minimum_hourly_on_demand_spend"
        ]
    if "current_on_demand_spend" in value:
        out["CurrentOnDemandSpend"] = value["current_on_demand_spend"]
    if "existing_hourly_commitment" in value:
        out["ExistingHourlyCommitment"] = value["existing_hourly_commitment"]
    if "hourly_commitment_to_purchase" in value:
        out["HourlyCommitmentToPurchase"] = value["hourly_commitment_to_purchase"]
    if "estimated_average_coverage" in value:
        out["EstimatedAverageCoverage"] = value["estimated_average_coverage"]
    if "estimated_average_utilization" in value:
        out["EstimatedAverageUtilization"] = value["estimated_average_utilization"]
    if "estimated_monthly_savings_amount" in value:
        out["EstimatedMonthlySavingsAmount"] = value["estimated_monthly_savings_amount"]
    if "estimated_on_demand_cost" in value:
        out["EstimatedOnDemandCost"] = value["estimated_on_demand_cost"]
    if "estimated_on_demand_cost_with_current_commitment" in value:
        out["EstimatedOnDemandCostWithCurrentCommitment"] = value[
            "estimated_on_demand_cost_with_current_commitment"
        ]
    if "estimated_roi" in value:
        out["EstimatedROI"] = value["estimated_roi"]
    if "estimated_savings_amount" in value:
        out["EstimatedSavingsAmount"] = value["estimated_savings_amount"]
    if "estimated_savings_percentage" in value:
        out["EstimatedSavingsPercentage"] = value["estimated_savings_percentage"]
    if "estimated_commitment_cost" in value:
        out["EstimatedCommitmentCost"] = value["estimated_commitment_cost"]
    if "latest_usage_timestamp" in value:
        out["LatestUsageTimestamp"] = value["latest_usage_timestamp"]
    if "upfront_cost" in value:
        out["UpfrontCost"] = value["upfront_cost"]
    if "additional_metadata" in value:
        out["AdditionalMetadata"] = value["additional_metadata"]
    if "metrics_over_lookback_period" in value:
        import capo_cost_explorer.types.metrics_over_lookback_period

        out["MetricsOverLookbackPeriod"] = (
            capo_cost_explorer.types.metrics_over_lookback_period.serialize_aws_json_1_1(
                value["metrics_over_lookback_period"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansPurchaseAnalysisDetails:
    out: SavingsPlansPurchaseAnalysisDetails = {}  # type: ignore[typeddict-item]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "LookbackPeriodInHours" in data:
        out["lookback_period_in_hours"] = data["LookbackPeriodInHours"]
    if "CurrentAverageCoverage" in data:
        out["current_average_coverage"] = data["CurrentAverageCoverage"]
    if "CurrentAverageHourlyOnDemandSpend" in data:
        out["current_average_hourly_on_demand_spend"] = data[
            "CurrentAverageHourlyOnDemandSpend"
        ]
    if "CurrentMaximumHourlyOnDemandSpend" in data:
        out["current_maximum_hourly_on_demand_spend"] = data[
            "CurrentMaximumHourlyOnDemandSpend"
        ]
    if "CurrentMinimumHourlyOnDemandSpend" in data:
        out["current_minimum_hourly_on_demand_spend"] = data[
            "CurrentMinimumHourlyOnDemandSpend"
        ]
    if "CurrentOnDemandSpend" in data:
        out["current_on_demand_spend"] = data["CurrentOnDemandSpend"]
    if "ExistingHourlyCommitment" in data:
        out["existing_hourly_commitment"] = data["ExistingHourlyCommitment"]
    if "HourlyCommitmentToPurchase" in data:
        out["hourly_commitment_to_purchase"] = data["HourlyCommitmentToPurchase"]
    if "EstimatedAverageCoverage" in data:
        out["estimated_average_coverage"] = data["EstimatedAverageCoverage"]
    if "EstimatedAverageUtilization" in data:
        out["estimated_average_utilization"] = data["EstimatedAverageUtilization"]
    if "EstimatedMonthlySavingsAmount" in data:
        out["estimated_monthly_savings_amount"] = data["EstimatedMonthlySavingsAmount"]
    if "EstimatedOnDemandCost" in data:
        out["estimated_on_demand_cost"] = data["EstimatedOnDemandCost"]
    if "EstimatedOnDemandCostWithCurrentCommitment" in data:
        out["estimated_on_demand_cost_with_current_commitment"] = data[
            "EstimatedOnDemandCostWithCurrentCommitment"
        ]
    if "EstimatedROI" in data:
        out["estimated_roi"] = data["EstimatedROI"]
    if "EstimatedSavingsAmount" in data:
        out["estimated_savings_amount"] = data["EstimatedSavingsAmount"]
    if "EstimatedSavingsPercentage" in data:
        out["estimated_savings_percentage"] = data["EstimatedSavingsPercentage"]
    if "EstimatedCommitmentCost" in data:
        out["estimated_commitment_cost"] = data["EstimatedCommitmentCost"]
    if "LatestUsageTimestamp" in data:
        out["latest_usage_timestamp"] = data["LatestUsageTimestamp"]
    if "UpfrontCost" in data:
        out["upfront_cost"] = data["UpfrontCost"]
    if "AdditionalMetadata" in data:
        out["additional_metadata"] = data["AdditionalMetadata"]
    if "MetricsOverLookbackPeriod" in data:
        import capo_cost_explorer.types.metrics_over_lookback_period

        out["metrics_over_lookback_period"] = (
            capo_cost_explorer.types.metrics_over_lookback_period.deserialize_aws_json_1_1(
                data["MetricsOverLookbackPeriod"]
            )
        )
    return out
