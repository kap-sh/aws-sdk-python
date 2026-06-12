"""Generated from Smithy shape ``com.amazonaws.lightsail#MetricStatisticList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.metric_statistic

MetricStatisticList: TypeAlias = list[
    "aws_sdk_lightsail.types.metric_statistic.MetricStatistic"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricStatisticList) -> list:
    import aws_sdk_lightsail.types.metric_statistic

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.metric_statistic.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MetricStatisticList:
    import aws_sdk_lightsail.types.metric_statistic

    out: MetricStatisticList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.metric_statistic.deserialize_aws_json_1_1(item)
        )
    return out
