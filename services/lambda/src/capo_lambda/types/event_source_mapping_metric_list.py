"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourceMappingMetricList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.event_source_mapping_metric

EventSourceMappingMetricList: TypeAlias = list[
    "capo_lambda.types.event_source_mapping_metric.EventSourceMappingMetric"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventSourceMappingMetricList) -> list:
    import capo_lambda.types.event_source_mapping_metric

    out: list = []
    for item in value:
        out.append(capo_lambda.types.event_source_mapping_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventSourceMappingMetricList:
    import capo_lambda.types.event_source_mapping_metric

    out: EventSourceMappingMetricList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.event_source_mapping_metric.deserialize_json(item))
    return out
