"""Generated from Smithy shape ``com.amazonaws.costexplorer#CoverageHours``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.coverage_hours_percentage
    import aws_sdk_cost_explorer.types.on_demand_hours
    import aws_sdk_cost_explorer.types.reserved_hours
    import aws_sdk_cost_explorer.types.total_running_hours


class CoverageHours(TypedDict, closed=True):
    on_demand_hours: NotRequired[
        "aws_sdk_cost_explorer.types.on_demand_hours.OnDemandHours"
    ]
    """<p>The number of instance running hours that On-Demand Instances covered.</p>"""
    reserved_hours: NotRequired[
        "aws_sdk_cost_explorer.types.reserved_hours.ReservedHours"
    ]
    """<p>The number of instance running hours that reservations covered.</p>"""
    total_running_hours: NotRequired[
        "aws_sdk_cost_explorer.types.total_running_hours.TotalRunningHours"
    ]
    """<p>The total instance usage, in hours.</p>"""
    coverage_hours_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.coverage_hours_percentage.CoverageHoursPercentage"
    ]
    """<p>The percentage of instance hours that a reservation covered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CoverageHours) -> dict:
    out: dict = {}
    if "on_demand_hours" in value:
        out["OnDemandHours"] = value["on_demand_hours"]
    if "reserved_hours" in value:
        out["ReservedHours"] = value["reserved_hours"]
    if "total_running_hours" in value:
        out["TotalRunningHours"] = value["total_running_hours"]
    if "coverage_hours_percentage" in value:
        out["CoverageHoursPercentage"] = value["coverage_hours_percentage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CoverageHours:
    out: CoverageHours = {}  # type: ignore[typeddict-item]
    if "OnDemandHours" in data:
        out["on_demand_hours"] = data["OnDemandHours"]
    if "ReservedHours" in data:
        out["reserved_hours"] = data["ReservedHours"]
    if "TotalRunningHours" in data:
        out["total_running_hours"] = data["TotalRunningHours"]
    if "CoverageHoursPercentage" in data:
        out["coverage_hours_percentage"] = data["CoverageHoursPercentage"]
    return out
