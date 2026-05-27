"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourceMappingMetricList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.event_source_mapping_metric

EventSourceMappingMetricList: TypeAlias = list[
    "aws_sdk_lambda.types.event_source_mapping_metric.EventSourceMappingMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventSourceMappingMetricList) -> list:
    import aws_sdk_lambda.types.event_source_mapping_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lambda.types.event_source_mapping_metric.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EventSourceMappingMetricList:
    import aws_sdk_lambda.types.event_source_mapping_metric

    out: EventSourceMappingMetricList = []
    for item in data:
        out.append(
            aws_sdk_lambda.types.event_source_mapping_metric.deserialize_json(item)
        )
    return out
