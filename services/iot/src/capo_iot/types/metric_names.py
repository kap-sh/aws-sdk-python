"""Generated from Smithy shape ``com.amazonaws.iot#MetricNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.metric_name

MetricNames: TypeAlias = list["capo_iot.types.metric_name.MetricName"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricNames) -> list:
    return list(value)


def deserialize_json(data: list) -> MetricNames:
    return list(data)
