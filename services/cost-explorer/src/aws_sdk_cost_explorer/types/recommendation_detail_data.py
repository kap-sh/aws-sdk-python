"""Generated from Smithy shape ``com.amazonaws.costexplorer#RecommendationDetailData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.account_scope
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.lookback_period_in_days
    import aws_sdk_cost_explorer.types.metrics_over_lookback_period
    import aws_sdk_cost_explorer.types.payment_option
    import aws_sdk_cost_explorer.types.supported_savings_plans_type
    import aws_sdk_cost_explorer.types.term_in_years
    import aws_sdk_cost_explorer.types.zoned_date_time


class RecommendationDetailData(TypedDict, closed=True):
    account_scope: NotRequired["aws_sdk_cost_explorer.types.account_scope.AccountScope"]
    """<p>The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to PAYER. If the value is LINKED, recommendations are calculated for individual member accounts only.</p>"""
    lookback_period_in_days: NotRequired[
        "aws_sdk_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays"
    ]
    """<p>How many days of previous usage that Amazon Web Services considers when making this recommendation.</p>"""
    savings_plans_type: NotRequired[
        "aws_sdk_cost_explorer.types.supported_savings_plans_type.SupportedSavingsPlansType"
    ]
    """<p>The requested Savings Plan recommendation type.</p>"""
    term_in_years: NotRequired["aws_sdk_cost_explorer.types.term_in_years.TermInYears"]
    """<p>The term of the commitment in years.</p>"""
    payment_option: NotRequired[
        "aws_sdk_cost_explorer.types.payment_option.PaymentOption"
    ]
    """<p>The payment option for the commitment (for example, All Upfront or No Upfront).</p>"""
    account_id: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The AccountID that the recommendation is generated for.</p>"""
    currency_code: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The currency code that Amazon Web Services used to generate the recommendation and present potential savings.</p>"""
    instance_family: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The instance family of the recommended Savings Plan.</p>"""
    region: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The region the recommendation is generated for.</p>"""
    offering_id: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The unique ID that's used to distinguish Savings Plans from one another.</p>"""
    generation_timestamp: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    latest_usage_timestamp: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    current_average_hourly_on_demand_spend: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The average value of hourly On-Demand spend over the lookback period of the applicable usage type.</p>"""
    current_maximum_hourly_on_demand_spend: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The highest value of hourly On-Demand spend over the lookback period of the applicable usage type.</p>"""
    current_minimum_hourly_on_demand_spend: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The lowest value of hourly On-Demand spend over the lookback period of the applicable usage type.</p>"""
    estimated_average_utilization: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated utilization of the recommended Savings Plan.</p>"""
    estimated_monthly_savings_amount: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated monthly savings amount based on the recommended Savings Plan.</p>"""
    estimated_on_demand_cost: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The remaining On-Demand cost estimated to not be covered by the recommended Savings Plan, over the length of the lookback period.</p>"""
    estimated_on_demand_cost_with_current_commitment: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated On-Demand costs you expect with no additional commitment, based on your usage of the selected time period and the Savings Plan you own.</p>"""
    estimated_roi: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated return on investment that's based on the recommended Savings Plan that you purchased. This is calculated as estimatedSavingsAmount/estimatedSPCost*100.</p>"""
    estimated_sp_cost: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The cost of the recommended Savings Plan over the length of the lookback period.</p>"""
    estimated_savings_amount: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated savings amount that's based on the recommended Savings Plan over the length of the lookback period.</p>"""
    estimated_savings_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated savings percentage relative to the total cost of applicable On-Demand usage over the lookback period.</p>"""
    existing_hourly_commitment: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The existing hourly commitment for the Savings Plan type.</p>"""
    hourly_commitment_to_purchase: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The recommended hourly commitment level for the Savings Plan type and the configuration that's based on the usage during the lookback period.</p>"""
    upfront_cost: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The upfront cost of the recommended Savings Plan, based on the selected payment option.</p>"""
    current_average_coverage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The average value of hourly coverage over the lookback period.</p>"""
    estimated_average_coverage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated coverage of the recommended Savings Plan.</p>"""
    metrics_over_lookback_period: NotRequired[
        "aws_sdk_cost_explorer.types.metrics_over_lookback_period.MetricsOverLookbackPeriod"
    ]
    """<p>The related hourly cost, coverage, and utilization metrics over the lookback period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationDetailData) -> dict:
    out: dict = {}
    if "account_scope" in value:
        import aws_sdk_cost_explorer.types.account_scope

        out["AccountScope"] = (
            aws_sdk_cost_explorer.types.account_scope.serialize_aws_json_1_1(
                value["account_scope"]
            )
        )
    if "lookback_period_in_days" in value:
        import aws_sdk_cost_explorer.types.lookback_period_in_days

        out["LookbackPeriodInDays"] = (
            aws_sdk_cost_explorer.types.lookback_period_in_days.serialize_aws_json_1_1(
                value["lookback_period_in_days"]
            )
        )
    if "savings_plans_type" in value:
        import aws_sdk_cost_explorer.types.supported_savings_plans_type

        out["SavingsPlansType"] = (
            aws_sdk_cost_explorer.types.supported_savings_plans_type.serialize_aws_json_1_1(
                value["savings_plans_type"]
            )
        )
    if "term_in_years" in value:
        import aws_sdk_cost_explorer.types.term_in_years

        out["TermInYears"] = (
            aws_sdk_cost_explorer.types.term_in_years.serialize_aws_json_1_1(
                value["term_in_years"]
            )
        )
    if "payment_option" in value:
        import aws_sdk_cost_explorer.types.payment_option

        out["PaymentOption"] = (
            aws_sdk_cost_explorer.types.payment_option.serialize_aws_json_1_1(
                value["payment_option"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    if "instance_family" in value:
        out["InstanceFamily"] = value["instance_family"]
    if "region" in value:
        out["Region"] = value["region"]
    if "offering_id" in value:
        out["OfferingId"] = value["offering_id"]
    if "generation_timestamp" in value:
        out["GenerationTimestamp"] = value["generation_timestamp"]
    if "latest_usage_timestamp" in value:
        out["LatestUsageTimestamp"] = value["latest_usage_timestamp"]
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
    if "estimated_sp_cost" in value:
        out["EstimatedSPCost"] = value["estimated_sp_cost"]
    if "estimated_savings_amount" in value:
        out["EstimatedSavingsAmount"] = value["estimated_savings_amount"]
    if "estimated_savings_percentage" in value:
        out["EstimatedSavingsPercentage"] = value["estimated_savings_percentage"]
    if "existing_hourly_commitment" in value:
        out["ExistingHourlyCommitment"] = value["existing_hourly_commitment"]
    if "hourly_commitment_to_purchase" in value:
        out["HourlyCommitmentToPurchase"] = value["hourly_commitment_to_purchase"]
    if "upfront_cost" in value:
        out["UpfrontCost"] = value["upfront_cost"]
    if "current_average_coverage" in value:
        out["CurrentAverageCoverage"] = value["current_average_coverage"]
    if "estimated_average_coverage" in value:
        out["EstimatedAverageCoverage"] = value["estimated_average_coverage"]
    if "metrics_over_lookback_period" in value:
        import aws_sdk_cost_explorer.types.metrics_over_lookback_period

        out["MetricsOverLookbackPeriod"] = (
            aws_sdk_cost_explorer.types.metrics_over_lookback_period.serialize_aws_json_1_1(
                value["metrics_over_lookback_period"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationDetailData:
    out: RecommendationDetailData = {}  # type: ignore[typeddict-item]
    if "AccountScope" in data:
        import aws_sdk_cost_explorer.types.account_scope

        out["account_scope"] = (
            aws_sdk_cost_explorer.types.account_scope.deserialize_aws_json_1_1(
                data["AccountScope"]
            )
        )
    if "LookbackPeriodInDays" in data:
        import aws_sdk_cost_explorer.types.lookback_period_in_days

        out["lookback_period_in_days"] = (
            aws_sdk_cost_explorer.types.lookback_period_in_days.deserialize_aws_json_1_1(
                data["LookbackPeriodInDays"]
            )
        )
    if "SavingsPlansType" in data:
        import aws_sdk_cost_explorer.types.supported_savings_plans_type

        out["savings_plans_type"] = (
            aws_sdk_cost_explorer.types.supported_savings_plans_type.deserialize_aws_json_1_1(
                data["SavingsPlansType"]
            )
        )
    if "TermInYears" in data:
        import aws_sdk_cost_explorer.types.term_in_years

        out["term_in_years"] = (
            aws_sdk_cost_explorer.types.term_in_years.deserialize_aws_json_1_1(
                data["TermInYears"]
            )
        )
    if "PaymentOption" in data:
        import aws_sdk_cost_explorer.types.payment_option

        out["payment_option"] = (
            aws_sdk_cost_explorer.types.payment_option.deserialize_aws_json_1_1(
                data["PaymentOption"]
            )
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "InstanceFamily" in data:
        out["instance_family"] = data["InstanceFamily"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "OfferingId" in data:
        out["offering_id"] = data["OfferingId"]
    if "GenerationTimestamp" in data:
        out["generation_timestamp"] = data["GenerationTimestamp"]
    if "LatestUsageTimestamp" in data:
        out["latest_usage_timestamp"] = data["LatestUsageTimestamp"]
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
    if "EstimatedSPCost" in data:
        out["estimated_sp_cost"] = data["EstimatedSPCost"]
    if "EstimatedSavingsAmount" in data:
        out["estimated_savings_amount"] = data["EstimatedSavingsAmount"]
    if "EstimatedSavingsPercentage" in data:
        out["estimated_savings_percentage"] = data["EstimatedSavingsPercentage"]
    if "ExistingHourlyCommitment" in data:
        out["existing_hourly_commitment"] = data["ExistingHourlyCommitment"]
    if "HourlyCommitmentToPurchase" in data:
        out["hourly_commitment_to_purchase"] = data["HourlyCommitmentToPurchase"]
    if "UpfrontCost" in data:
        out["upfront_cost"] = data["UpfrontCost"]
    if "CurrentAverageCoverage" in data:
        out["current_average_coverage"] = data["CurrentAverageCoverage"]
    if "EstimatedAverageCoverage" in data:
        out["estimated_average_coverage"] = data["EstimatedAverageCoverage"]
    if "MetricsOverLookbackPeriod" in data:
        import aws_sdk_cost_explorer.types.metrics_over_lookback_period

        out["metrics_over_lookback_period"] = (
            aws_sdk_cost_explorer.types.metrics_over_lookback_period.deserialize_aws_json_1_1(
                data["MetricsOverLookbackPeriod"]
            )
        )
    return out
