"""Generated from Smithy shape ``com.amazonaws.connect#CurrentMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.current_metric

CurrentMetrics: TypeAlias = list["capo_connect.types.current_metric.CurrentMetric"]


# --- restJson1 ser/de ---
def serialize_json(value: CurrentMetrics) -> list:
    import capo_connect.types.current_metric

    out: list = []
    for item in value:
        out.append(capo_connect.types.current_metric.serialize_json(item))
    return out


def deserialize_json(data: list) -> CurrentMetrics:
    import capo_connect.types.current_metric

    out: CurrentMetrics = []
    for item in data:
        out.append(capo_connect.types.current_metric.deserialize_json(item))
    return out
