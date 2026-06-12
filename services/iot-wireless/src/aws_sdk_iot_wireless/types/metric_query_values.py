"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricQueryValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.metric_query_value

MetricQueryValues: TypeAlias = list[
    "aws_sdk_iot_wireless.types.metric_query_value.MetricQueryValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryValues) -> list:
    import aws_sdk_iot_wireless.types.metric_query_value

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_wireless.types.metric_query_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricQueryValues:
    import aws_sdk_iot_wireless.types.metric_query_value

    out: MetricQueryValues = []
    for item in data:
        out.append(aws_sdk_iot_wireless.types.metric_query_value.deserialize_json(item))
    return out
