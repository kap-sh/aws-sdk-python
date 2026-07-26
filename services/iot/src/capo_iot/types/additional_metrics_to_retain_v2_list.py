"""Generated from Smithy shape ``com.amazonaws.iot#AdditionalMetricsToRetainV2List``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.metric_to_retain

AdditionalMetricsToRetainV2List: TypeAlias = list[
    "capo_iot.types.metric_to_retain.MetricToRetain"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalMetricsToRetainV2List) -> list:
    import capo_iot.types.metric_to_retain

    out: list = []
    for item in value:
        out.append(capo_iot.types.metric_to_retain.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdditionalMetricsToRetainV2List:
    import capo_iot.types.metric_to_retain

    out: AdditionalMetricsToRetainV2List = []
    for item in data:
        out.append(capo_iot.types.metric_to_retain.deserialize_json(item))
    return out
