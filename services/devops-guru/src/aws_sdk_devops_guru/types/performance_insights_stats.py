"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsStats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.performance_insights_stat

PerformanceInsightsStats: TypeAlias = list[
    "aws_sdk_devops_guru.types.performance_insights_stat.PerformanceInsightsStat"
]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsStats) -> list:
    import aws_sdk_devops_guru.types.performance_insights_stat

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.performance_insights_stat.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PerformanceInsightsStats:
    import aws_sdk_devops_guru.types.performance_insights_stat

    out: PerformanceInsightsStats = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.performance_insights_stat.deserialize_json(item)
        )
    return out
