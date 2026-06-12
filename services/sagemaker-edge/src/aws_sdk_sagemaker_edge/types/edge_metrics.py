"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#EdgeMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_edge.types.edge_metric

EdgeMetrics: TypeAlias = list["aws_sdk_sagemaker_edge.types.edge_metric.EdgeMetric"]


# --- restJson1 ser/de ---
def serialize_json(value: EdgeMetrics) -> list:
    import aws_sdk_sagemaker_edge.types.edge_metric

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker_edge.types.edge_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> EdgeMetrics:
    import aws_sdk_sagemaker_edge.types.edge_metric

    out: EdgeMetrics = []
    for item in data:
        out.append(aws_sdk_sagemaker_edge.types.edge_metric.deserialize_json(item))
    return out
