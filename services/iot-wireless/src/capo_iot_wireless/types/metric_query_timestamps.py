"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricQueryTimestamps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.metric_query_timestamp

MetricQueryTimestamps: TypeAlias = list[
    "capo_iot_wireless.types.metric_query_timestamp.MetricQueryTimestamp"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryTimestamps) -> list:
    import capo_iot_wireless.types.metric_query_timestamp

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.metric_query_timestamp.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricQueryTimestamps:
    import capo_iot_wireless.types.metric_query_timestamp

    out: MetricQueryTimestamps = []
    for item in data:
        out.append(
            capo_iot_wireless.types.metric_query_timestamp.deserialize_json(item)
        )
    return out
