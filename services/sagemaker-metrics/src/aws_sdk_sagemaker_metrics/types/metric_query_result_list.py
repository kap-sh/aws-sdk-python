"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#MetricQueryResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_metrics.types.metric_query_result

MetricQueryResultList: TypeAlias = list[
    "aws_sdk_sagemaker_metrics.types.metric_query_result.MetricQueryResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryResultList) -> list:
    import aws_sdk_sagemaker_metrics.types.metric_query_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker_metrics.types.metric_query_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MetricQueryResultList:
    import aws_sdk_sagemaker_metrics.types.metric_query_result

    out: MetricQueryResultList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker_metrics.types.metric_query_result.deserialize_json(item)
        )
    return out
