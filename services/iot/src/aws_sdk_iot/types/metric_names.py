"""Generated from Smithy shape ``com.amazonaws.iot#MetricNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.metric_name

MetricNames: TypeAlias = list["aws_sdk_iot.types.metric_name.MetricName"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricNames) -> list:
    return list(value)


def deserialize_json(data: list) -> MetricNames:
    return list(data)
