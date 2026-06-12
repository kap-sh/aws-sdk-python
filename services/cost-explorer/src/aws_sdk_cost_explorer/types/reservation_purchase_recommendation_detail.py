"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationPurchaseRecommendationDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.instance_details
    import aws_sdk_cost_explorer.types.reserved_capacity_details


class ReservationPurchaseRecommendationDetail(TypedDict):
    account_id: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The account that this Reserved Instance (RI) recommendation is for.</p>"""
    instance_details: NotRequired[
        "aws_sdk_cost_explorer.types.instance_details.InstanceDetails"
    ]
    """<p>Details about the reservations that Amazon Web Services recommends that you purchase.</p>"""
    recommended_number_of_instances_to_purchase: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The number of instances that Amazon Web Services recommends that you purchase.</p>"""
    recommended_normalized_units_to_purchase: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The number of normalized units that Amazon Web Services recommends that you purchase.</p>"""
    minimum_number_of_instances_used_per_hour: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The minimum number of instances that you used in an hour during the historical period. Amazon Web Services uses this to calculate your recommended reservation purchases.</p>"""
    minimum_normalized_units_used_per_hour: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The minimum number of normalized units that you used in an hour during the historical period. Amazon Web Services uses this to calculate your recommended reservation purchases.</p>"""
    maximum_number_of_instances_used_per_hour: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum number of instances that you used in an hour during the historical period. Amazon Web Services uses this to calculate your recommended reservation purchases.</p>"""
    maximum_normalized_units_used_per_hour: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum number of normalized units that you used in an hour during the historical period. Amazon Web Services uses this to calculate your recommended reservation purchases.</p>"""
    average_number_of_instances_used_per_hour: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The average number of instances that you used in an hour during the historical period. Amazon Web Services uses this to calculate your recommended reservation purchases.</p>"""
    average_normalized_units_used_per_hour: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The average number of normalized units that you used in an hour during the historical period. Amazon Web Services uses this to calculate your recommended reservation purchases.</p>"""
    average_utilization: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The average utilization of your instances. Amazon Web Services uses this to calculate your recommended reservation purchases.</p>"""
    estimated_break_even_in_months: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>How long Amazon Web Services estimates that it takes for this instance to start saving you money, in months.</p>"""
    currency_code: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The currency code that Amazon Web Services used to calculate the costs for this instance.</p>"""
    estimated_monthly_savings_amount: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>How much Amazon Web Services estimates that this specific recommendation might save you in a month.</p>"""
    estimated_monthly_savings_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>How much Amazon Web Services estimates that this specific recommendation might save you in a month, as a percentage of your overall costs.</p>"""
    estimated_monthly_on_demand_cost: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>How much Amazon Web Services estimates that you spend on On-Demand Instances in a month.</p>"""
    estimated_reservation_cost_for_lookback_period: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>How much Amazon Web Services estimates that you might spend for all usage during the specified historical period if you had a reservation.</p>"""
    upfront_cost: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>How much purchasing this instance costs you upfront.</p>"""
    recurring_standard_monthly_cost: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>How much purchasing this instance costs you on a monthly basis.</p>"""
    reserved_capacity_details: NotRequired[
        "aws_sdk_cost_explorer.types.reserved_capacity_details.ReservedCapacityDetails"
    ]
    """<p>Details about the reservations that Amazon Web Services recommends that you purchase.</p>"""
    recommended_number_of_capacity_units_to_purchase: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The number of reserved capacity units that Amazon Web Services recommends that you purchase.</p>"""
    minimum_number_of_capacity_units_used_per_hour: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The minimum number of provisioned capacity units that you used in an hour during the historical period. Amazon Web Services uses this to calculate your recommended reservation purchases.</p>"""
    maximum_number_of_capacity_units_used_per_hour: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum number of provisioned capacity units that you used in an hour during the historical period. Amazon Web Services uses this to calculate your recommended reservation purchases.</p>"""
    average_number_of_capacity_units_used_per_hour: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The average number of provisioned capacity units that you used in an hour during the historical period. Amazon Web Services uses this to calculate your recommended reservation purchases.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationPurchaseRecommendationDetail) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "instance_details" in value:
        import aws_sdk_cost_explorer.types.instance_details

        out["InstanceDetails"] = (
            aws_sdk_cost_explorer.types.instance_details.serialize_aws_json_1_1(
                value["instance_details"]
            )
        )
    if "recommended_number_of_instances_to_purchase" in value:
        out["RecommendedNumberOfInstancesToPurchase"] = value[
            "recommended_number_of_instances_to_purchase"
        ]
    if "recommended_normalized_units_to_purchase" in value:
        out["RecommendedNormalizedUnitsToPurchase"] = value[
            "recommended_normalized_units_to_purchase"
        ]
    if "minimum_number_of_instances_used_per_hour" in value:
        out["MinimumNumberOfInstancesUsedPerHour"] = value[
            "minimum_number_of_instances_used_per_hour"
        ]
    if "minimum_normalized_units_used_per_hour" in value:
        out["MinimumNormalizedUnitsUsedPerHour"] = value[
            "minimum_normalized_units_used_per_hour"
        ]
    if "maximum_number_of_instances_used_per_hour" in value:
        out["MaximumNumberOfInstancesUsedPerHour"] = value[
            "maximum_number_of_instances_used_per_hour"
        ]
    if "maximum_normalized_units_used_per_hour" in value:
        out["MaximumNormalizedUnitsUsedPerHour"] = value[
            "maximum_normalized_units_used_per_hour"
        ]
    if "average_number_of_instances_used_per_hour" in value:
        out["AverageNumberOfInstancesUsedPerHour"] = value[
            "average_number_of_instances_used_per_hour"
        ]
    if "average_normalized_units_used_per_hour" in value:
        out["AverageNormalizedUnitsUsedPerHour"] = value[
            "average_normalized_units_used_per_hour"
        ]
    if "average_utilization" in value:
        out["AverageUtilization"] = value["average_utilization"]
    if "estimated_break_even_in_months" in value:
        out["EstimatedBreakEvenInMonths"] = value["estimated_break_even_in_months"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    if "estimated_monthly_savings_amount" in value:
        out["EstimatedMonthlySavingsAmount"] = value["estimated_monthly_savings_amount"]
    if "estimated_monthly_savings_percentage" in value:
        out["EstimatedMonthlySavingsPercentage"] = value[
            "estimated_monthly_savings_percentage"
        ]
    if "estimated_monthly_on_demand_cost" in value:
        out["EstimatedMonthlyOnDemandCost"] = value["estimated_monthly_on_demand_cost"]
    if "estimated_reservation_cost_for_lookback_period" in value:
        out["EstimatedReservationCostForLookbackPeriod"] = value[
            "estimated_reservation_cost_for_lookback_period"
        ]
    if "upfront_cost" in value:
        out["UpfrontCost"] = value["upfront_cost"]
    if "recurring_standard_monthly_cost" in value:
        out["RecurringStandardMonthlyCost"] = value["recurring_standard_monthly_cost"]
    if "reserved_capacity_details" in value:
        import aws_sdk_cost_explorer.types.reserved_capacity_details

        out["ReservedCapacityDetails"] = (
            aws_sdk_cost_explorer.types.reserved_capacity_details.serialize_aws_json_1_1(
                value["reserved_capacity_details"]
            )
        )
    if "recommended_number_of_capacity_units_to_purchase" in value:
        out["RecommendedNumberOfCapacityUnitsToPurchase"] = value[
            "recommended_number_of_capacity_units_to_purchase"
        ]
    if "minimum_number_of_capacity_units_used_per_hour" in value:
        out["MinimumNumberOfCapacityUnitsUsedPerHour"] = value[
            "minimum_number_of_capacity_units_used_per_hour"
        ]
    if "maximum_number_of_capacity_units_used_per_hour" in value:
        out["MaximumNumberOfCapacityUnitsUsedPerHour"] = value[
            "maximum_number_of_capacity_units_used_per_hour"
        ]
    if "average_number_of_capacity_units_used_per_hour" in value:
        out["AverageNumberOfCapacityUnitsUsedPerHour"] = value[
            "average_number_of_capacity_units_used_per_hour"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservationPurchaseRecommendationDetail:
    out: ReservationPurchaseRecommendationDetail = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "InstanceDetails" in data:
        import aws_sdk_cost_explorer.types.instance_details

        out["instance_details"] = (
            aws_sdk_cost_explorer.types.instance_details.deserialize_aws_json_1_1(
                data["InstanceDetails"]
            )
        )
    if "RecommendedNumberOfInstancesToPurchase" in data:
        out["recommended_number_of_instances_to_purchase"] = data[
            "RecommendedNumberOfInstancesToPurchase"
        ]
    if "RecommendedNormalizedUnitsToPurchase" in data:
        out["recommended_normalized_units_to_purchase"] = data[
            "RecommendedNormalizedUnitsToPurchase"
        ]
    if "MinimumNumberOfInstancesUsedPerHour" in data:
        out["minimum_number_of_instances_used_per_hour"] = data[
            "MinimumNumberOfInstancesUsedPerHour"
        ]
    if "MinimumNormalizedUnitsUsedPerHour" in data:
        out["minimum_normalized_units_used_per_hour"] = data[
            "MinimumNormalizedUnitsUsedPerHour"
        ]
    if "MaximumNumberOfInstancesUsedPerHour" in data:
        out["maximum_number_of_instances_used_per_hour"] = data[
            "MaximumNumberOfInstancesUsedPerHour"
        ]
    if "MaximumNormalizedUnitsUsedPerHour" in data:
        out["maximum_normalized_units_used_per_hour"] = data[
            "MaximumNormalizedUnitsUsedPerHour"
        ]
    if "AverageNumberOfInstancesUsedPerHour" in data:
        out["average_number_of_instances_used_per_hour"] = data[
            "AverageNumberOfInstancesUsedPerHour"
        ]
    if "AverageNormalizedUnitsUsedPerHour" in data:
        out["average_normalized_units_used_per_hour"] = data[
            "AverageNormalizedUnitsUsedPerHour"
        ]
    if "AverageUtilization" in data:
        out["average_utilization"] = data["AverageUtilization"]
    if "EstimatedBreakEvenInMonths" in data:
        out["estimated_break_even_in_months"] = data["EstimatedBreakEvenInMonths"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "EstimatedMonthlySavingsAmount" in data:
        out["estimated_monthly_savings_amount"] = data["EstimatedMonthlySavingsAmount"]
    if "EstimatedMonthlySavingsPercentage" in data:
        out["estimated_monthly_savings_percentage"] = data[
            "EstimatedMonthlySavingsPercentage"
        ]
    if "EstimatedMonthlyOnDemandCost" in data:
        out["estimated_monthly_on_demand_cost"] = data["EstimatedMonthlyOnDemandCost"]
    if "EstimatedReservationCostForLookbackPeriod" in data:
        out["estimated_reservation_cost_for_lookback_period"] = data[
            "EstimatedReservationCostForLookbackPeriod"
        ]
    if "UpfrontCost" in data:
        out["upfront_cost"] = data["UpfrontCost"]
    if "RecurringStandardMonthlyCost" in data:
        out["recurring_standard_monthly_cost"] = data["RecurringStandardMonthlyCost"]
    if "ReservedCapacityDetails" in data:
        import aws_sdk_cost_explorer.types.reserved_capacity_details

        out["reserved_capacity_details"] = (
            aws_sdk_cost_explorer.types.reserved_capacity_details.deserialize_aws_json_1_1(
                data["ReservedCapacityDetails"]
            )
        )
    if "RecommendedNumberOfCapacityUnitsToPurchase" in data:
        out["recommended_number_of_capacity_units_to_purchase"] = data[
            "RecommendedNumberOfCapacityUnitsToPurchase"
        ]
    if "MinimumNumberOfCapacityUnitsUsedPerHour" in data:
        out["minimum_number_of_capacity_units_used_per_hour"] = data[
            "MinimumNumberOfCapacityUnitsUsedPerHour"
        ]
    if "MaximumNumberOfCapacityUnitsUsedPerHour" in data:
        out["maximum_number_of_capacity_units_used_per_hour"] = data[
            "MaximumNumberOfCapacityUnitsUsedPerHour"
        ]
    if "AverageNumberOfCapacityUnitsUsedPerHour" in data:
        out["average_number_of_capacity_units_used_per_hour"] = data[
            "AverageNumberOfCapacityUnitsUsedPerHour"
        ]
    return out
