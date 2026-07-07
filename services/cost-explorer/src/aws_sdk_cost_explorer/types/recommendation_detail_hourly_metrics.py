"""Generated from Smithy shape ``com.amazonaws.costexplorer#RecommendationDetailHourlyMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.zoned_date_time


class RecommendationDetailHourlyMetrics(TypedDict, closed=True):
    start_time: NotRequired["aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"]
    estimated_on_demand_cost: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The remaining On-Demand cost estimated to not be covered by the recommended Savings Plan, over the length of the lookback period.</p>"""
    current_coverage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The current amount of Savings Plans eligible usage that the Savings Plan covered.</p>"""
    estimated_coverage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated coverage amount based on the recommended Savings Plan.</p>"""
    estimated_new_commitment_utilization: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated utilization for the recommended Savings Plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationDetailHourlyMetrics) -> dict:
    out: dict = {}
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    if "estimated_on_demand_cost" in value:
        out["EstimatedOnDemandCost"] = value["estimated_on_demand_cost"]
    if "current_coverage" in value:
        out["CurrentCoverage"] = value["current_coverage"]
    if "estimated_coverage" in value:
        out["EstimatedCoverage"] = value["estimated_coverage"]
    if "estimated_new_commitment_utilization" in value:
        out["EstimatedNewCommitmentUtilization"] = value[
            "estimated_new_commitment_utilization"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationDetailHourlyMetrics:
    out: RecommendationDetailHourlyMetrics = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    if "EstimatedOnDemandCost" in data:
        out["estimated_on_demand_cost"] = data["EstimatedOnDemandCost"]
    if "CurrentCoverage" in data:
        out["current_coverage"] = data["CurrentCoverage"]
    if "EstimatedCoverage" in data:
        out["estimated_coverage"] = data["EstimatedCoverage"]
    if "EstimatedNewCommitmentUtilization" in data:
        out["estimated_new_commitment_utilization"] = data[
            "EstimatedNewCommitmentUtilization"
        ]
    return out
