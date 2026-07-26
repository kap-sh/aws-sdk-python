"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#WorkloadInsightsTopContributorsRowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.workload_insights_top_contributors_row

WorkloadInsightsTopContributorsRowList: TypeAlias = list[
    "capo_networkflowmonitor.types.workload_insights_top_contributors_row.WorkloadInsightsTopContributorsRow"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadInsightsTopContributorsRowList) -> list:
    import capo_networkflowmonitor.types.workload_insights_top_contributors_row

    out: list = []
    for item in value:
        out.append(
            capo_networkflowmonitor.types.workload_insights_top_contributors_row.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WorkloadInsightsTopContributorsRowList:
    import capo_networkflowmonitor.types.workload_insights_top_contributors_row

    out: WorkloadInsightsTopContributorsRowList = []
    for item in data:
        out.append(
            capo_networkflowmonitor.types.workload_insights_top_contributors_row.deserialize_json(
                item
            )
        )
    return out
