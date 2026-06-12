"""Generated from Smithy shape ``com.amazonaws.iot#AdditionalMetricsToRetainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.behavior_metric

AdditionalMetricsToRetainList: TypeAlias = list[
    "aws_sdk_iot.types.behavior_metric.BehaviorMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalMetricsToRetainList) -> list:
    return list(value)


def deserialize_json(data: list) -> AdditionalMetricsToRetainList:
    return list(data)
