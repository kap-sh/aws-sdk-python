"""Generated from Smithy shape ``com.amazonaws.costexplorer#CoverageNormalizedUnits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.coverage_normalized_units_percentage
    import aws_sdk_cost_explorer.types.on_demand_normalized_units
    import aws_sdk_cost_explorer.types.reserved_normalized_units
    import aws_sdk_cost_explorer.types.total_running_normalized_units


class CoverageNormalizedUnits(TypedDict, closed=True):
    on_demand_normalized_units: NotRequired[
        "aws_sdk_cost_explorer.types.on_demand_normalized_units.OnDemandNormalizedUnits"
    ]
    """<p>The number of normalized units that are covered by On-Demand Instances instead of a reservation.</p>"""
    reserved_normalized_units: NotRequired[
        "aws_sdk_cost_explorer.types.reserved_normalized_units.ReservedNormalizedUnits"
    ]
    """<p>The number of normalized units that a reservation covers.</p>"""
    total_running_normalized_units: NotRequired[
        "aws_sdk_cost_explorer.types.total_running_normalized_units.TotalRunningNormalizedUnits"
    ]
    """<p>The total number of normalized units that you used.</p>"""
    coverage_normalized_units_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.coverage_normalized_units_percentage.CoverageNormalizedUnitsPercentage"
    ]
    """<p>The percentage of your used instance normalized units that a reservation covers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CoverageNormalizedUnits) -> dict:
    out: dict = {}
    if "on_demand_normalized_units" in value:
        out["OnDemandNormalizedUnits"] = value["on_demand_normalized_units"]
    if "reserved_normalized_units" in value:
        out["ReservedNormalizedUnits"] = value["reserved_normalized_units"]
    if "total_running_normalized_units" in value:
        out["TotalRunningNormalizedUnits"] = value["total_running_normalized_units"]
    if "coverage_normalized_units_percentage" in value:
        out["CoverageNormalizedUnitsPercentage"] = value[
            "coverage_normalized_units_percentage"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CoverageNormalizedUnits:
    out: CoverageNormalizedUnits = {}  # type: ignore[typeddict-item]
    if "OnDemandNormalizedUnits" in data:
        out["on_demand_normalized_units"] = data["OnDemandNormalizedUnits"]
    if "ReservedNormalizedUnits" in data:
        out["reserved_normalized_units"] = data["ReservedNormalizedUnits"]
    if "TotalRunningNormalizedUnits" in data:
        out["total_running_normalized_units"] = data["TotalRunningNormalizedUnits"]
    if "CoverageNormalizedUnitsPercentage" in data:
        out["coverage_normalized_units_percentage"] = data[
            "CoverageNormalizedUnitsPercentage"
        ]
    return out
