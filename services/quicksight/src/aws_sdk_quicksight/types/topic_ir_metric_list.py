"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRMetricList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_ir_metric

TopicIRMetricList: TypeAlias = list[
    "aws_sdk_quicksight.types.topic_ir_metric.TopicIRMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRMetricList) -> list:
    import aws_sdk_quicksight.types.topic_ir_metric

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.topic_ir_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicIRMetricList:
    import aws_sdk_quicksight.types.topic_ir_metric

    out: TopicIRMetricList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.topic_ir_metric.deserialize_json(item))
    return out
