"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_metrics.types.long
    import capo_sagemaker_metrics.types.metric_name
    import capo_sagemaker_metrics.types.metric_statistic
    import capo_sagemaker_metrics.types.period
    import capo_sagemaker_metrics.types.sage_maker_resource_arn
    import capo_sagemaker_metrics.types.x_axis_type


class MetricQuery(TypedDict, closed=True):
    metric_name: NotRequired["capo_sagemaker_metrics.types.metric_name.MetricName"]
    """<p>The name of the metric to retrieve.</p>"""
    resource_arn: NotRequired[
        "capo_sagemaker_metrics.types.sage_maker_resource_arn.SageMakerResourceArn"
    ]
    """<p>The ARN of the SageMaker resource to retrieve metrics for.</p>"""
    metric_stat: NotRequired[
        "capo_sagemaker_metrics.types.metric_statistic.MetricStatistic"
    ]
    """<p>The metrics stat type of metrics to retrieve.</p>"""
    period: NotRequired["capo_sagemaker_metrics.types.period.Period"]
    """<p>The time period of metrics to retrieve.</p>"""
    x_axis_type: NotRequired["capo_sagemaker_metrics.types.x_axis_type.XAxisType"]
    """<p>The x-axis type of metrics to retrieve.</p>"""
    start: NotRequired["capo_sagemaker_metrics.types.long.Long"]
    """<p>The start time of metrics to retrieve.</p>"""
    end: NotRequired["capo_sagemaker_metrics.types.long.Long"]
    """<p>The end time of metrics to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricQuery) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "metric_stat" in value:
        import capo_sagemaker_metrics.types.metric_statistic

        out["MetricStat"] = (
            capo_sagemaker_metrics.types.metric_statistic.serialize_json(
                value["metric_stat"]
            )
        )
    if "period" in value:
        import capo_sagemaker_metrics.types.period

        out["Period"] = capo_sagemaker_metrics.types.period.serialize_json(
            value["period"]
        )
    if "x_axis_type" in value:
        import capo_sagemaker_metrics.types.x_axis_type

        out["XAxisType"] = capo_sagemaker_metrics.types.x_axis_type.serialize_json(
            value["x_axis_type"]
        )
    if "start" in value:
        out["Start"] = value["start"]
    if "end" in value:
        out["End"] = value["end"]
    return out


def deserialize_json(data: dict) -> MetricQuery:
    out: MetricQuery = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "MetricStat" in data:
        import capo_sagemaker_metrics.types.metric_statistic

        out["metric_stat"] = (
            capo_sagemaker_metrics.types.metric_statistic.deserialize_json(
                data["MetricStat"]
            )
        )
    if "Period" in data:
        import capo_sagemaker_metrics.types.period

        out["period"] = capo_sagemaker_metrics.types.period.deserialize_json(
            data["Period"]
        )
    if "XAxisType" in data:
        import capo_sagemaker_metrics.types.x_axis_type

        out["x_axis_type"] = capo_sagemaker_metrics.types.x_axis_type.deserialize_json(
            data["XAxisType"]
        )
    if "Start" in data:
        out["start"] = data["Start"]
    if "End" in data:
        out["end"] = data["End"]
    return out
