"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricQueryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_metrics.types.metric_query

MetricQueryList: TypeAlias = list[
    "capo_sagemaker_metrics.types.metric_query.MetricQuery"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryList) -> list:
    import capo_sagemaker_metrics.types.metric_query

    out: list = []
    for item in value:
        out.append(capo_sagemaker_metrics.types.metric_query.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricQueryList:
    import capo_sagemaker_metrics.types.metric_query

    out: MetricQueryList = []
    for item in data:
        out.append(capo_sagemaker_metrics.types.metric_query.deserialize_json(item))
    return out
