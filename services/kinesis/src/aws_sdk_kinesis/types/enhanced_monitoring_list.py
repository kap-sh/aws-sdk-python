"""Generated from Smithy shape ``com.amazonaws.kinesis#EnhancedMonitoringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.enhanced_metrics

EnhancedMonitoringList: TypeAlias = list[
    "aws_sdk_kinesis.types.enhanced_metrics.EnhancedMetrics"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnhancedMonitoringList) -> list:
    import aws_sdk_kinesis.types.enhanced_metrics

    out: list = []
    for item in value:
        out.append(aws_sdk_kinesis.types.enhanced_metrics.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EnhancedMonitoringList:
    import aws_sdk_kinesis.types.enhanced_metrics

    out: EnhancedMonitoringList = []
    for item in data:
        out.append(
            aws_sdk_kinesis.types.enhanced_metrics.deserialize_aws_json_1_1(item)
        )
    return out
