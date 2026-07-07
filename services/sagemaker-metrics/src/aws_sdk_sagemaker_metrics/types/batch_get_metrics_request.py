"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#BatchGetMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_metrics.types.metric_query_list


class BatchGetMetricsRequest(TypedDict, closed=True):
    metric_queries: NotRequired[
        "aws_sdk_sagemaker_metrics.types.metric_query_list.MetricQueryList"
    ]
    """<p>Queries made to retrieve training metrics from SageMaker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMetricsRequest) -> dict:
    out: dict = {}
    if "metric_queries" in value:
        import aws_sdk_sagemaker_metrics.types.metric_query_list

        out["MetricQueries"] = (
            aws_sdk_sagemaker_metrics.types.metric_query_list.serialize_json(
                value["metric_queries"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetMetricsRequest:
    out: BatchGetMetricsRequest = {}  # type: ignore[typeddict-item]
    if "MetricQueries" in data:
        import aws_sdk_sagemaker_metrics.types.metric_query_list

        out["metric_queries"] = (
            aws_sdk_sagemaker_metrics.types.metric_query_list.deserialize_json(
                data["MetricQueries"]
            )
        )
    return out
