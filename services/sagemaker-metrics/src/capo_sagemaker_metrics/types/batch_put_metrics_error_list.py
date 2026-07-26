"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#BatchPutMetricsErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_metrics.types.batch_put_metrics_error

BatchPutMetricsErrorList: TypeAlias = list[
    "capo_sagemaker_metrics.types.batch_put_metrics_error.BatchPutMetricsError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutMetricsErrorList) -> list:
    import capo_sagemaker_metrics.types.batch_put_metrics_error

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker_metrics.types.batch_put_metrics_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchPutMetricsErrorList:
    import capo_sagemaker_metrics.types.batch_put_metrics_error

    out: BatchPutMetricsErrorList = []
    for item in data:
        out.append(
            capo_sagemaker_metrics.types.batch_put_metrics_error.deserialize_json(item)
        )
    return out
