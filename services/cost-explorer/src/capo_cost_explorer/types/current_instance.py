"""Generated from Smithy shape ``com.amazonaws.costexplorer#CurrentInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.resource_details
    import capo_cost_explorer.types.resource_utilization
    import capo_cost_explorer.types.tag_values_list


class CurrentInstance(TypedDict, closed=True):
    resource_id: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>Resource ID of the current instance.</p>"""
    instance_name: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The name that you given an instance. This field shows as blank if you haven't given the instance a name.</p>"""
    tags: NotRequired["capo_cost_explorer.types.tag_values_list.TagValuesList"]
    """<p>Cost allocation resource tags that are applied to the instance.</p>"""
    resource_details: NotRequired[
        "capo_cost_explorer.types.resource_details.ResourceDetails"
    ]
    """<p>Details about the resource and utilization.</p>"""
    resource_utilization: NotRequired[
        "capo_cost_explorer.types.resource_utilization.ResourceUtilization"
    ]
    """<p>Utilization information of the current instance during the lookback period.</p>"""
    reservation_covered_hours_in_lookback_period: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The number of hours during the lookback period that's covered by reservations.</p>"""
    savings_plans_covered_hours_in_lookback_period: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The number of hours during the lookback period that's covered by Savings Plans.</p>"""
    on_demand_hours_in_lookback_period: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The number of hours during the lookback period that's billed at On-Demand rates.</p>"""
    total_running_hours_in_lookback_period: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The total number of hours that the instance ran during the lookback period.</p>"""
    monthly_cost: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The current On-Demand cost of operating this instance on a monthly basis.</p>"""
    currency_code: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The currency code that Amazon Web Services used to calculate the costs for this instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CurrentInstance) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "instance_name" in value:
        out["InstanceName"] = value["instance_name"]
    if "tags" in value:
        import capo_cost_explorer.types.tag_values_list

        out["Tags"] = capo_cost_explorer.types.tag_values_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "resource_details" in value:
        import capo_cost_explorer.types.resource_details

        out["ResourceDetails"] = (
            capo_cost_explorer.types.resource_details.serialize_aws_json_1_1(
                value["resource_details"]
            )
        )
    if "resource_utilization" in value:
        import capo_cost_explorer.types.resource_utilization

        out["ResourceUtilization"] = (
            capo_cost_explorer.types.resource_utilization.serialize_aws_json_1_1(
                value["resource_utilization"]
            )
        )
    if "reservation_covered_hours_in_lookback_period" in value:
        out["ReservationCoveredHoursInLookbackPeriod"] = value[
            "reservation_covered_hours_in_lookback_period"
        ]
    if "savings_plans_covered_hours_in_lookback_period" in value:
        out["SavingsPlansCoveredHoursInLookbackPeriod"] = value[
            "savings_plans_covered_hours_in_lookback_period"
        ]
    if "on_demand_hours_in_lookback_period" in value:
        out["OnDemandHoursInLookbackPeriod"] = value[
            "on_demand_hours_in_lookback_period"
        ]
    if "total_running_hours_in_lookback_period" in value:
        out["TotalRunningHoursInLookbackPeriod"] = value[
            "total_running_hours_in_lookback_period"
        ]
    if "monthly_cost" in value:
        out["MonthlyCost"] = value["monthly_cost"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CurrentInstance:
    out: CurrentInstance = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "InstanceName" in data:
        out["instance_name"] = data["InstanceName"]
    if "Tags" in data:
        import capo_cost_explorer.types.tag_values_list

        out["tags"] = capo_cost_explorer.types.tag_values_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ResourceDetails" in data:
        import capo_cost_explorer.types.resource_details

        out["resource_details"] = (
            capo_cost_explorer.types.resource_details.deserialize_aws_json_1_1(
                data["ResourceDetails"]
            )
        )
    if "ResourceUtilization" in data:
        import capo_cost_explorer.types.resource_utilization

        out["resource_utilization"] = (
            capo_cost_explorer.types.resource_utilization.deserialize_aws_json_1_1(
                data["ResourceUtilization"]
            )
        )
    if "ReservationCoveredHoursInLookbackPeriod" in data:
        out["reservation_covered_hours_in_lookback_period"] = data[
            "ReservationCoveredHoursInLookbackPeriod"
        ]
    if "SavingsPlansCoveredHoursInLookbackPeriod" in data:
        out["savings_plans_covered_hours_in_lookback_period"] = data[
            "SavingsPlansCoveredHoursInLookbackPeriod"
        ]
    if "OnDemandHoursInLookbackPeriod" in data:
        out["on_demand_hours_in_lookback_period"] = data[
            "OnDemandHoursInLookbackPeriod"
        ]
    if "TotalRunningHoursInLookbackPeriod" in data:
        out["total_running_hours_in_lookback_period"] = data[
            "TotalRunningHoursInLookbackPeriod"
        ]
    if "MonthlyCost" in data:
        out["monthly_cost"] = data["MonthlyCost"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    return out
