"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricQueryResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_metrics.types.metric_query_result

MetricQueryResultList: TypeAlias = list[
    "capo_sagemaker_metrics.types.metric_query_result.MetricQueryResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryResultList) -> list:
    import capo_sagemaker_metrics.types.metric_query_result

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker_metrics.types.metric_query_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MetricQueryResultList:
    import capo_sagemaker_metrics.types.metric_query_result

    out: MetricQueryResultList = []
    for item in data:
        out.append(
            capo_sagemaker_metrics.types.metric_query_result.deserialize_json(item)
        )
    return out
