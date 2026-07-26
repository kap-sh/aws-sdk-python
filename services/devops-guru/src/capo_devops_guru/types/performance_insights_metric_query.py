"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsMetricQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.performance_insights_metric_dimension_group
    import capo_devops_guru.types.performance_insights_metric_filter_map
    import capo_devops_guru.types.performance_insights_metric_name


class PerformanceInsightsMetricQuery(TypedDict, closed=True):
    metric: NotRequired[
        "capo_devops_guru.types.performance_insights_metric_name.PerformanceInsightsMetricName"
    ]
    """<p>The name of the meteric used used when querying an Performance Insights <code>GetResourceMetrics</code> API for anomaly metrics.</p> <p>Valid values for <code>Metric</code> are:</p> <ul> <li> <p> <code>db.load.avg</code> - a scaled representation of the number of active sessions for the database engine.</p> </li> <li> <p> <code>db.sampledload.avg</code> - the raw number of active sessions for the database engine.</p> </li> </ul> <p>If the number of active sessions is less than an internal Performance Insights threshold, <code>db.load.avg</code> and <code>db.sampledload.avg</code> are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with <code>db.load.avg</code> showing the scaled values, <code>db.sampledload.avg</code> showing the raw values, and <code>db.sampledload.avg</code> less than <code>db.load.avg</code>. For most use cases, you can query <code>db.load.avg</code> only. </p>"""
    group_by: NotRequired[
        "capo_devops_guru.types.performance_insights_metric_dimension_group.PerformanceInsightsMetricDimensionGroup"
    ]
    """<p>The specification for how to aggregate the data points from a Performance Insights <code>GetResourceMetrics</code> API query. The Performance Insights query returns all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.</p>"""
    filter: NotRequired[
        "capo_devops_guru.types.performance_insights_metric_filter_map.PerformanceInsightsMetricFilterMap"
    ]
    """<p>One or more filters to apply to a Performance Insights <code>GetResourceMetrics</code> API query. Restrictions:</p> <ul> <li> <p>Any number of filters by the same dimension, as specified in the <code>GroupBy</code> parameter.</p> </li> <li> <p>A single filter for any other dimension in this dimension group.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsMetricQuery) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "group_by" in value:
        import capo_devops_guru.types.performance_insights_metric_dimension_group

        out["GroupBy"] = (
            capo_devops_guru.types.performance_insights_metric_dimension_group.serialize_json(
                value["group_by"]
            )
        )
    if "filter" in value:
        import capo_devops_guru.types.performance_insights_metric_filter_map

        out["Filter"] = (
            capo_devops_guru.types.performance_insights_metric_filter_map.serialize_json(
                value["filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> PerformanceInsightsMetricQuery:
    out: PerformanceInsightsMetricQuery = {}  # type: ignore[typeddict-item]
    if "Metric" in data:
        out["metric"] = data["Metric"]
    if "GroupBy" in data:
        import capo_devops_guru.types.performance_insights_metric_dimension_group

        out["group_by"] = (
            capo_devops_guru.types.performance_insights_metric_dimension_group.deserialize_json(
                data["GroupBy"]
            )
        )
    if "Filter" in data:
        import capo_devops_guru.types.performance_insights_metric_filter_map

        out["filter"] = (
            capo_devops_guru.types.performance_insights_metric_filter_map.deserialize_json(
                data["Filter"]
            )
        )
    return out
