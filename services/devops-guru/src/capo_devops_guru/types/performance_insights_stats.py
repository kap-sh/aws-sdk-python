"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsStats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.performance_insights_stat

PerformanceInsightsStats: TypeAlias = list[
    "capo_devops_guru.types.performance_insights_stat.PerformanceInsightsStat"
]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsStats) -> list:
    import capo_devops_guru.types.performance_insights_stat

    out: list = []
    for item in value:
        out.append(
            capo_devops_guru.types.performance_insights_stat.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PerformanceInsightsStats:
    import capo_devops_guru.types.performance_insights_stat

    out: PerformanceInsightsStats = []
    for item in data:
        out.append(
            capo_devops_guru.types.performance_insights_stat.deserialize_json(item)
        )
    return out
