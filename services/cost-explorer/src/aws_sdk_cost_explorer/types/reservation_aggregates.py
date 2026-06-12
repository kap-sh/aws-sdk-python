"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationAggregates``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.amortized_recurring_fee
    import aws_sdk_cost_explorer.types.amortized_upfront_fee
    import aws_sdk_cost_explorer.types.net_ri_savings
    import aws_sdk_cost_explorer.types.on_demand_cost_of_ri_hours_used
    import aws_sdk_cost_explorer.types.purchased_hours
    import aws_sdk_cost_explorer.types.purchased_units
    import aws_sdk_cost_explorer.types.realized_savings
    import aws_sdk_cost_explorer.types.ri_cost_for_unused_hours
    import aws_sdk_cost_explorer.types.total_actual_hours
    import aws_sdk_cost_explorer.types.total_actual_units
    import aws_sdk_cost_explorer.types.total_amortized_fee
    import aws_sdk_cost_explorer.types.total_potential_ri_savings
    import aws_sdk_cost_explorer.types.unrealized_savings
    import aws_sdk_cost_explorer.types.unused_hours
    import aws_sdk_cost_explorer.types.unused_units
    import aws_sdk_cost_explorer.types.utilization_percentage
    import aws_sdk_cost_explorer.types.utilization_percentage_in_units


class ReservationAggregates(TypedDict):
    utilization_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.utilization_percentage.UtilizationPercentage"
    ]
    """<p>The percentage of reservation time that you used.</p>"""
    utilization_percentage_in_units: NotRequired[
        "aws_sdk_cost_explorer.types.utilization_percentage_in_units.UtilizationPercentageInUnits"
    ]
    """<p>The percentage of Amazon EC2 reservation time that you used. It's converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.</p>"""
    purchased_hours: NotRequired[
        "aws_sdk_cost_explorer.types.purchased_hours.PurchasedHours"
    ]
    """<p>How many reservation hours that you purchased.</p>"""
    purchased_units: NotRequired[
        "aws_sdk_cost_explorer.types.purchased_units.PurchasedUnits"
    ]
    """<p>The number of Amazon EC2 reservation hours that you purchased. It's converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.</p>"""
    total_actual_hours: NotRequired[
        "aws_sdk_cost_explorer.types.total_actual_hours.TotalActualHours"
    ]
    """<p>The total number of reservation hours that you used.</p>"""
    total_actual_units: NotRequired[
        "aws_sdk_cost_explorer.types.total_actual_units.TotalActualUnits"
    ]
    """<p>The total number of Amazon EC2 reservation hours that you used. It's converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.</p>"""
    unused_hours: NotRequired["aws_sdk_cost_explorer.types.unused_hours.UnusedHours"]
    """<p>The number of reservation hours that you didn't use.</p>"""
    unused_units: NotRequired["aws_sdk_cost_explorer.types.unused_units.UnusedUnits"]
    """<p>The number of Amazon EC2 reservation hours that you didn't use. It's converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.</p>"""
    on_demand_cost_of_ri_hours_used: NotRequired[
        "aws_sdk_cost_explorer.types.on_demand_cost_of_ri_hours_used.OnDemandCostOfRIHoursUsed"
    ]
    """<p>How much your reservation costs if charged On-Demand rates.</p>"""
    net_ri_savings: NotRequired[
        "aws_sdk_cost_explorer.types.net_ri_savings.NetRISavings"
    ]
    """<p>How much you saved due to purchasing and utilizing reservation. Amazon Web Services calculates this by subtracting <code>TotalAmortizedFee</code> from <code>OnDemandCostOfRIHoursUsed</code>.</p>"""
    total_potential_ri_savings: NotRequired[
        "aws_sdk_cost_explorer.types.total_potential_ri_savings.TotalPotentialRISavings"
    ]
    """<p>How much you might save if you use your entire reservation.</p>"""
    amortized_upfront_fee: NotRequired[
        "aws_sdk_cost_explorer.types.amortized_upfront_fee.AmortizedUpfrontFee"
    ]
    """<p>The upfront cost of your reservation. It's amortized over the reservation period.</p>"""
    amortized_recurring_fee: NotRequired[
        "aws_sdk_cost_explorer.types.amortized_recurring_fee.AmortizedRecurringFee"
    ]
    """<p>The monthly cost of your reservation. It's amortized over the reservation period.</p>"""
    total_amortized_fee: NotRequired[
        "aws_sdk_cost_explorer.types.total_amortized_fee.TotalAmortizedFee"
    ]
    """<p>The total cost of your reservation. It's amortized over the reservation period.</p>"""
    ri_cost_for_unused_hours: NotRequired[
        "aws_sdk_cost_explorer.types.ri_cost_for_unused_hours.RICostForUnusedHours"
    ]
    """<p>The cost of unused hours for your reservation.</p>"""
    realized_savings: NotRequired[
        "aws_sdk_cost_explorer.types.realized_savings.RealizedSavings"
    ]
    """<p>The realized savings because of purchasing and using a reservation.</p>"""
    unrealized_savings: NotRequired[
        "aws_sdk_cost_explorer.types.unrealized_savings.UnrealizedSavings"
    ]
    """<p>The unrealized savings because of purchasing and using a reservation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationAggregates) -> dict:
    out: dict = {}
    if "utilization_percentage" in value:
        out["UtilizationPercentage"] = value["utilization_percentage"]
    if "utilization_percentage_in_units" in value:
        out["UtilizationPercentageInUnits"] = value["utilization_percentage_in_units"]
    if "purchased_hours" in value:
        out["PurchasedHours"] = value["purchased_hours"]
    if "purchased_units" in value:
        out["PurchasedUnits"] = value["purchased_units"]
    if "total_actual_hours" in value:
        out["TotalActualHours"] = value["total_actual_hours"]
    if "total_actual_units" in value:
        out["TotalActualUnits"] = value["total_actual_units"]
    if "unused_hours" in value:
        out["UnusedHours"] = value["unused_hours"]
    if "unused_units" in value:
        out["UnusedUnits"] = value["unused_units"]
    if "on_demand_cost_of_ri_hours_used" in value:
        out["OnDemandCostOfRIHoursUsed"] = value["on_demand_cost_of_ri_hours_used"]
    if "net_ri_savings" in value:
        out["NetRISavings"] = value["net_ri_savings"]
    if "total_potential_ri_savings" in value:
        out["TotalPotentialRISavings"] = value["total_potential_ri_savings"]
    if "amortized_upfront_fee" in value:
        out["AmortizedUpfrontFee"] = value["amortized_upfront_fee"]
    if "amortized_recurring_fee" in value:
        out["AmortizedRecurringFee"] = value["amortized_recurring_fee"]
    if "total_amortized_fee" in value:
        out["TotalAmortizedFee"] = value["total_amortized_fee"]
    if "ri_cost_for_unused_hours" in value:
        out["RICostForUnusedHours"] = value["ri_cost_for_unused_hours"]
    if "realized_savings" in value:
        out["RealizedSavings"] = value["realized_savings"]
    if "unrealized_savings" in value:
        out["UnrealizedSavings"] = value["unrealized_savings"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservationAggregates:
    out: ReservationAggregates = {}  # type: ignore[typeddict-item]
    if "UtilizationPercentage" in data:
        out["utilization_percentage"] = data["UtilizationPercentage"]
    if "UtilizationPercentageInUnits" in data:
        out["utilization_percentage_in_units"] = data["UtilizationPercentageInUnits"]
    if "PurchasedHours" in data:
        out["purchased_hours"] = data["PurchasedHours"]
    if "PurchasedUnits" in data:
        out["purchased_units"] = data["PurchasedUnits"]
    if "TotalActualHours" in data:
        out["total_actual_hours"] = data["TotalActualHours"]
    if "TotalActualUnits" in data:
        out["total_actual_units"] = data["TotalActualUnits"]
    if "UnusedHours" in data:
        out["unused_hours"] = data["UnusedHours"]
    if "UnusedUnits" in data:
        out["unused_units"] = data["UnusedUnits"]
    if "OnDemandCostOfRIHoursUsed" in data:
        out["on_demand_cost_of_ri_hours_used"] = data["OnDemandCostOfRIHoursUsed"]
    if "NetRISavings" in data:
        out["net_ri_savings"] = data["NetRISavings"]
    if "TotalPotentialRISavings" in data:
        out["total_potential_ri_savings"] = data["TotalPotentialRISavings"]
    if "AmortizedUpfrontFee" in data:
        out["amortized_upfront_fee"] = data["AmortizedUpfrontFee"]
    if "AmortizedRecurringFee" in data:
        out["amortized_recurring_fee"] = data["AmortizedRecurringFee"]
    if "TotalAmortizedFee" in data:
        out["total_amortized_fee"] = data["TotalAmortizedFee"]
    if "RICostForUnusedHours" in data:
        out["ri_cost_for_unused_hours"] = data["RICostForUnusedHours"]
    if "RealizedSavings" in data:
        out["realized_savings"] = data["RealizedSavings"]
    if "UnrealizedSavings" in data:
        out["unrealized_savings"] = data["UnrealizedSavings"]
    return out
