"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsMetricFilterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.performance_insights_metric_filter_key
    import capo_devops_guru.types.performance_insights_metric_filter_value

PerformanceInsightsMetricFilterMap: TypeAlias = dict[
    "capo_devops_guru.types.performance_insights_metric_filter_key.PerformanceInsightsMetricFilterKey",
    "capo_devops_guru.types.performance_insights_metric_filter_value.PerformanceInsightsMetricFilterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PerformanceInsightsMetricFilterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PerformanceInsightsMetricFilterMap:
    out: PerformanceInsightsMetricFilterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
