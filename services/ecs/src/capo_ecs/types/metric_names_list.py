"""Generated from Smithy shape ``com.amazonaws.ecs#MetricNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.metric_name

MetricNamesList: TypeAlias = list["capo_ecs.types.metric_name.MetricName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MetricNamesList:
    return [item for item in data if item is not None]
