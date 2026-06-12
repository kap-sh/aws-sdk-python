"""Generated from Smithy shape ``com.amazonaws.connect#CurrentMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.current_metric

CurrentMetrics: TypeAlias = list["aws_sdk_connect.types.current_metric.CurrentMetric"]


# --- restJson1 ser/de ---
def serialize_json(value: CurrentMetrics) -> list:
    import aws_sdk_connect.types.current_metric

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.current_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> CurrentMetrics:
    import aws_sdk_connect.types.current_metric

    out: CurrentMetrics = []
    for item in data:
        out.append(aws_sdk_connect.types.current_metric.deserialize_json(item))
    return out
