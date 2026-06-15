"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsMetricsDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.performance_insights_metric_display_name
    import aws_sdk_devops_guru.types.performance_insights_metric_query
    import aws_sdk_devops_guru.types.performance_insights_metric_unit
    import aws_sdk_devops_guru.types.performance_insights_reference_data_list
    import aws_sdk_devops_guru.types.performance_insights_stats


class PerformanceInsightsMetricsDetail(TypedDict):
    metric_display_name: NotRequired[
        "aws_sdk_devops_guru.types.performance_insights_metric_display_name.PerformanceInsightsMetricDisplayName"
    ]
    """<p>The name used for a specific Performance Insights metric.</p>"""
    unit: NotRequired[
        "aws_sdk_devops_guru.types.performance_insights_metric_unit.PerformanceInsightsMetricUnit"
    ]
    """<p>The unit of measure for a metric. For example, a session or a process.</p>"""
    metric_query: NotRequired[
        "aws_sdk_devops_guru.types.performance_insights_metric_query.PerformanceInsightsMetricQuery"
    ]
    r"""<p>A single query to be processed for the metric. For more information, see <code> <a href=\"https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsMetricQuery.html\">PerformanceInsightsMetricQuery</a> </code>.</p>"""
    reference_data: NotRequired[
        "aws_sdk_devops_guru.types.performance_insights_reference_data_list.PerformanceInsightsReferenceDataList"
    ]
    r"""<p> For more information, see <code> <a href=\"https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_PerformanceInsightsReferenceData.html\">PerformanceInsightsReferenceData</a> </code>. </p>"""
    stats_at_anomaly: NotRequired[
        "aws_sdk_devops_guru.types.performance_insights_stats.PerformanceInsightsStats"
    ]
    """<p>The metric statistics during the anomalous period detected by DevOps Guru;</p>"""
    stats_at_baseline: NotRequired[
        "aws_sdk_devops_guru.types.performance_insights_stats.PerformanceInsightsStats"
    ]
    """<p>Typical metric statistics that are not considered anomalous. When DevOps Guru analyzes metrics, it compares them to <code>StatsAtBaseline</code> to help determine if they are anomalous.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsMetricsDetail) -> dict:
    out: dict = {}
    if "metric_display_name" in value:
        out["MetricDisplayName"] = value["metric_display_name"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    if "metric_query" in value:
        import aws_sdk_devops_guru.types.performance_insights_metric_query

        out["MetricQuery"] = (
            aws_sdk_devops_guru.types.performance_insights_metric_query.serialize_json(
                value["metric_query"]
            )
        )
    if "reference_data" in value:
        import aws_sdk_devops_guru.types.performance_insights_reference_data_list

        out["ReferenceData"] = (
            aws_sdk_devops_guru.types.performance_insights_reference_data_list.serialize_json(
                value["reference_data"]
            )
        )
    if "stats_at_anomaly" in value:
        import aws_sdk_devops_guru.types.performance_insights_stats

        out["StatsAtAnomaly"] = (
            aws_sdk_devops_guru.types.performance_insights_stats.serialize_json(
                value["stats_at_anomaly"]
            )
        )
    if "stats_at_baseline" in value:
        import aws_sdk_devops_guru.types.performance_insights_stats

        out["StatsAtBaseline"] = (
            aws_sdk_devops_guru.types.performance_insights_stats.serialize_json(
                value["stats_at_baseline"]
            )
        )
    return out


def deserialize_json(data: dict) -> PerformanceInsightsMetricsDetail:
    out: PerformanceInsightsMetricsDetail = {}  # type: ignore[typeddict-item]
    if "MetricDisplayName" in data:
        out["metric_display_name"] = data["MetricDisplayName"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    if "MetricQuery" in data:
        import aws_sdk_devops_guru.types.performance_insights_metric_query

        out["metric_query"] = (
            aws_sdk_devops_guru.types.performance_insights_metric_query.deserialize_json(
                data["MetricQuery"]
            )
        )
    if "ReferenceData" in data:
        import aws_sdk_devops_guru.types.performance_insights_reference_data_list

        out["reference_data"] = (
            aws_sdk_devops_guru.types.performance_insights_reference_data_list.deserialize_json(
                data["ReferenceData"]
            )
        )
    if "StatsAtAnomaly" in data:
        import aws_sdk_devops_guru.types.performance_insights_stats

        out["stats_at_anomaly"] = (
            aws_sdk_devops_guru.types.performance_insights_stats.deserialize_json(
                data["StatsAtAnomaly"]
            )
        )
    if "StatsAtBaseline" in data:
        import aws_sdk_devops_guru.types.performance_insights_stats

        out["stats_at_baseline"] = (
            aws_sdk_devops_guru.types.performance_insights_stats.deserialize_json(
                data["StatsAtBaseline"]
            )
        )
    return out
