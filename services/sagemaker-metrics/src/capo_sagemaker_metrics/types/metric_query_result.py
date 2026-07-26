"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricQueryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_metrics.types.message
    import capo_sagemaker_metrics.types.metric_query_result_status
    import capo_sagemaker_metrics.types.metric_values
    import capo_sagemaker_metrics.types.x_axis_values


class MetricQueryResult(TypedDict, closed=True):
    status: NotRequired[
        "capo_sagemaker_metrics.types.metric_query_result_status.MetricQueryResultStatus"
    ]
    """<p>The status of the metric query.</p>"""
    message: NotRequired["capo_sagemaker_metrics.types.message.Message"]
    """<p>A message describing the status of the metric query.</p>"""
    x_axis_values: NotRequired["capo_sagemaker_metrics.types.x_axis_values.XAxisValues"]
    """<p>The values for the x-axis of the metrics.</p>"""
    metric_values: NotRequired[
        "capo_sagemaker_metrics.types.metric_values.MetricValues"
    ]
    """<p>The metric values retrieved by the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryResult) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_sagemaker_metrics.types.metric_query_result_status

        out["Status"] = (
            capo_sagemaker_metrics.types.metric_query_result_status.serialize_json(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "x_axis_values" in value:
        import capo_sagemaker_metrics.types.x_axis_values

        out["XAxisValues"] = capo_sagemaker_metrics.types.x_axis_values.serialize_json(
            value["x_axis_values"]
        )
    if "metric_values" in value:
        import capo_sagemaker_metrics.types.metric_values

        out["MetricValues"] = capo_sagemaker_metrics.types.metric_values.serialize_json(
            value["metric_values"]
        )
    return out


def deserialize_json(data: dict) -> MetricQueryResult:
    out: MetricQueryResult = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_sagemaker_metrics.types.metric_query_result_status

        out["status"] = (
            capo_sagemaker_metrics.types.metric_query_result_status.deserialize_json(
                data["Status"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "XAxisValues" in data:
        import capo_sagemaker_metrics.types.x_axis_values

        out["x_axis_values"] = (
            capo_sagemaker_metrics.types.x_axis_values.deserialize_json(
                data["XAxisValues"]
            )
        )
    if "MetricValues" in data:
        import capo_sagemaker_metrics.types.metric_values

        out["metric_values"] = (
            capo_sagemaker_metrics.types.metric_values.deserialize_json(
                data["MetricValues"]
            )
        )
    return out
