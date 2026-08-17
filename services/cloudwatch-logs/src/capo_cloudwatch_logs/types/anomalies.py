"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Anomalies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.anomaly

Anomalies: TypeAlias = list["capo_cloudwatch_logs.types.anomaly.Anomaly"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Anomalies) -> list:
    import capo_cloudwatch_logs.types.anomaly

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.anomaly.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Anomalies:
    import capo_cloudwatch_logs.types.anomaly

    out: Anomalies = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch_logs.types.anomaly.deserialize_aws_json_1_1(item))
    return out
