"""Generated from Smithy shape ``com.amazonaws.pi#MetricKeyDataPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.metric_key_data_points

MetricKeyDataPointsList: TypeAlias = list[
    "aws_sdk_pi.types.metric_key_data_points.MetricKeyDataPoints"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricKeyDataPointsList) -> list:
    import aws_sdk_pi.types.metric_key_data_points

    out: list = []
    for item in value:
        out.append(aws_sdk_pi.types.metric_key_data_points.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricKeyDataPointsList:
    import aws_sdk_pi.types.metric_key_data_points

    out: MetricKeyDataPointsList = []
    for item in data:
        out.append(
            aws_sdk_pi.types.metric_key_data_points.deserialize_aws_json_1_1(item)
        )
    return out
