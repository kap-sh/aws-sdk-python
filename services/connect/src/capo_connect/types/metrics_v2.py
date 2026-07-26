"""Generated from Smithy shape ``com.amazonaws.connect#MetricsV2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.metric_v2

MetricsV2: TypeAlias = list["capo_connect.types.metric_v2.MetricV2"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricsV2) -> list:
    import capo_connect.types.metric_v2

    out: list = []
    for item in value:
        out.append(capo_connect.types.metric_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricsV2:
    import capo_connect.types.metric_v2

    out: MetricsV2 = []
    for item in data:
        out.append(capo_connect.types.metric_v2.deserialize_json(item))
    return out
