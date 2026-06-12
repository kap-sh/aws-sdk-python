"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricQueryTimestamps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.metric_query_timestamp

MetricQueryTimestamps: TypeAlias = list[
    "aws_sdk_iot_wireless.types.metric_query_timestamp.MetricQueryTimestamp"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryTimestamps) -> list:
    import aws_sdk_iot_wireless.types.metric_query_timestamp

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_wireless.types.metric_query_timestamp.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MetricQueryTimestamps:
    import aws_sdk_iot_wireless.types.metric_query_timestamp

    out: MetricQueryTimestamps = []
    for item in data:
        out.append(
            aws_sdk_iot_wireless.types.metric_query_timestamp.deserialize_json(item)
        )
    return out
