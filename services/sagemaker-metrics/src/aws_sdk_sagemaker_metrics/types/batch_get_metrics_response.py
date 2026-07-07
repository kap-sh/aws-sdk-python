"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#BatchGetMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker_metrics.types.metric_query_result_list


class BatchGetMetricsResponse(TypedDict, closed=True):
    metric_query_results: NotRequired[
        "aws_sdk_sagemaker_metrics.types.metric_query_result_list.MetricQueryResultList"
    ]
    """<p>The results of a query to retrieve training metrics from SageMaker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMetricsResponse) -> dict:
    out: dict = {}
    if "metric_query_results" in value:
        import aws_sdk_sagemaker_metrics.types.metric_query_result_list

        out["MetricQueryResults"] = (
            aws_sdk_sagemaker_metrics.types.metric_query_result_list.serialize_json(
                value["metric_query_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetMetricsResponse:
    out: BatchGetMetricsResponse = {}  # type: ignore[typeddict-item]
    if "MetricQueryResults" in data:
        import aws_sdk_sagemaker_metrics.types.metric_query_result_list

        out["metric_query_results"] = (
            aws_sdk_sagemaker_metrics.types.metric_query_result_list.deserialize_json(
                data["MetricQueryResults"]
            )
        )
    return out
