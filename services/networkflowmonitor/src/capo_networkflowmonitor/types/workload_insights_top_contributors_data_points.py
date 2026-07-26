"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#WorkloadInsightsTopContributorsDataPoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.workload_insights_top_contributors_data_point

WorkloadInsightsTopContributorsDataPoints: TypeAlias = list[
    "capo_networkflowmonitor.types.workload_insights_top_contributors_data_point.WorkloadInsightsTopContributorsDataPoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadInsightsTopContributorsDataPoints) -> list:
    import capo_networkflowmonitor.types.workload_insights_top_contributors_data_point

    out: list = []
    for item in value:
        out.append(
            capo_networkflowmonitor.types.workload_insights_top_contributors_data_point.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WorkloadInsightsTopContributorsDataPoints:
    import capo_networkflowmonitor.types.workload_insights_top_contributors_data_point

    out: WorkloadInsightsTopContributorsDataPoints = []
    for item in data:
        out.append(
            capo_networkflowmonitor.types.workload_insights_top_contributors_data_point.deserialize_json(
                item
            )
        )
    return out
