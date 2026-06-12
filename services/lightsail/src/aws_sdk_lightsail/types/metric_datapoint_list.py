"""Generated from Smithy shape ``com.amazonaws.lightsail#MetricDatapointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.metric_datapoint

MetricDatapointList: TypeAlias = list[
    "aws_sdk_lightsail.types.metric_datapoint.MetricDatapoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDatapointList) -> list:
    import aws_sdk_lightsail.types.metric_datapoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.metric_datapoint.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MetricDatapointList:
    import aws_sdk_lightsail.types.metric_datapoint

    out: MetricDatapointList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.metric_datapoint.deserialize_aws_json_1_1(item)
        )
    return out
