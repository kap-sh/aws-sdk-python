"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#BatchPutMetricsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_metrics.types.batch_put_metrics_error_list


class BatchPutMetricsResponse(TypedDict):
    errors: NotRequired[
        "aws_sdk_sagemaker_metrics.types.batch_put_metrics_error_list.BatchPutMetricsErrorList"
    ]
    """<p>Lists any errors that occur when inserting metric data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutMetricsResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_sagemaker_metrics.types.batch_put_metrics_error_list

        out["Errors"] = (
            aws_sdk_sagemaker_metrics.types.batch_put_metrics_error_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchPutMetricsResponse:
    out: BatchPutMetricsResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_sagemaker_metrics.types.batch_put_metrics_error_list

        out["errors"] = (
            aws_sdk_sagemaker_metrics.types.batch_put_metrics_error_list.deserialize_json(
                data["Errors"]
            )
        )
    return out
