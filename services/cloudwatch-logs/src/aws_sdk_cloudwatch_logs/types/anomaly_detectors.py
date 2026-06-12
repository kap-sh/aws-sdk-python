"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AnomalyDetectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.anomaly_detector

AnomalyDetectors: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.anomaly_detector.AnomalyDetector"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalyDetectors) -> list:
    import aws_sdk_cloudwatch_logs.types.anomaly_detector

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.anomaly_detector.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AnomalyDetectors:
    import aws_sdk_cloudwatch_logs.types.anomaly_detector

    out: AnomalyDetectors = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.anomaly_detector.deserialize_aws_json_1_1(
                item
            )
        )
    return out
