"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#BatchPutMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_metrics.types.batch_put_metrics_error_list


class BatchPutMetricsResponse(TypedDict, closed=True):
    errors: NotRequired[
        "capo_sagemaker_metrics.types.batch_put_metrics_error_list.BatchPutMetricsErrorList"
    ]
    """<p>Lists any errors that occur when inserting metric data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutMetricsResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_sagemaker_metrics.types.batch_put_metrics_error_list

        out["Errors"] = (
            capo_sagemaker_metrics.types.batch_put_metrics_error_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchPutMetricsResponse:
    out: BatchPutMetricsResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import capo_sagemaker_metrics.types.batch_put_metrics_error_list

        out["errors"] = (
            capo_sagemaker_metrics.types.batch_put_metrics_error_list.deserialize_json(
                data["Errors"]
            )
        )
    return out
