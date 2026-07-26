"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#BatchPutMetricsError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_metrics.types.integer
    import capo_sagemaker_metrics.types.put_metrics_error_code


class BatchPutMetricsError(TypedDict, closed=True):
    code: NotRequired[
        "capo_sagemaker_metrics.types.put_metrics_error_code.PutMetricsErrorCode"
    ]
    """<p>The error code of an error that occured when attempting to put metrics.</p> <ul> <li> <p> <code>METRIC_LIMIT_EXCEEDED</code>: The maximum amount of metrics per resource is exceeded.</p> </li> <li> <p> <code>INTERNAL_ERROR</code>: An internal error occured.</p> </li> <li> <p> <code>VALIDATION_ERROR</code>: The metric data failed validation.</p> </li> <li> <p> <code>CONFLICT_ERROR</code>: Multiple requests attempted to modify the same data simultaneously.</p> </li> </ul>"""
    metric_index: NotRequired["capo_sagemaker_metrics.types.integer.Integer"]
    """<p>An index that corresponds to the metric in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutMetricsError) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_sagemaker_metrics.types.put_metrics_error_code

        out["Code"] = (
            capo_sagemaker_metrics.types.put_metrics_error_code.serialize_json(
                value["code"]
            )
        )
    if "metric_index" in value:
        out["MetricIndex"] = value["metric_index"]
    return out


def deserialize_json(data: dict) -> BatchPutMetricsError:
    out: BatchPutMetricsError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_sagemaker_metrics.types.put_metrics_error_code

        out["code"] = (
            capo_sagemaker_metrics.types.put_metrics_error_code.deserialize_json(
                data["Code"]
            )
        )
    if "MetricIndex" in data:
        out["metric_index"] = data["MetricIndex"]
    return out
