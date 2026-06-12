"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricQueryResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_metrics.types.message
    import aws_sdk_sagemaker_metrics.types.metric_query_result_status
    import aws_sdk_sagemaker_metrics.types.metric_values
    import aws_sdk_sagemaker_metrics.types.x_axis_values


class MetricQueryResult(TypedDict):
    status: NotRequired[
        "aws_sdk_sagemaker_metrics.types.metric_query_result_status.MetricQueryResultStatus"
    ]
    """<p>The status of the metric query.</p>"""
    message: NotRequired["aws_sdk_sagemaker_metrics.types.message.Message"]
    """<p>A message describing the status of the metric query.</p>"""
    x_axis_values: NotRequired[
        "aws_sdk_sagemaker_metrics.types.x_axis_values.XAxisValues"
    ]
    """<p>The values for the x-axis of the metrics.</p>"""
    metric_values: NotRequired[
        "aws_sdk_sagemaker_metrics.types.metric_values.MetricValues"
    ]
    """<p>The metric values retrieved by the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryResult) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker_metrics.types.metric_query_result_status

        out["Status"] = (
            aws_sdk_sagemaker_metrics.types.metric_query_result_status.serialize_json(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "x_axis_values" in value:
        import aws_sdk_sagemaker_metrics.types.x_axis_values

        out["XAxisValues"] = (
            aws_sdk_sagemaker_metrics.types.x_axis_values.serialize_json(
                value["x_axis_values"]
            )
        )
    if "metric_values" in value:
        import aws_sdk_sagemaker_metrics.types.metric_values

        out["MetricValues"] = (
            aws_sdk_sagemaker_metrics.types.metric_values.serialize_json(
                value["metric_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetricQueryResult:
    out: MetricQueryResult = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker_metrics.types.metric_query_result_status

        out["status"] = (
            aws_sdk_sagemaker_metrics.types.metric_query_result_status.deserialize_json(
                data["Status"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "XAxisValues" in data:
        import aws_sdk_sagemaker_metrics.types.x_axis_values

        out["x_axis_values"] = (
            aws_sdk_sagemaker_metrics.types.x_axis_values.deserialize_json(
                data["XAxisValues"]
            )
        )
    if "MetricValues" in data:
        import aws_sdk_sagemaker_metrics.types.metric_values

        out["metric_values"] = (
            aws_sdk_sagemaker_metrics.types.metric_values.deserialize_json(
                data["MetricValues"]
            )
        )
    return out
