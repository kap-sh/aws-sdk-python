"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseMetricName``."""

from typing import Literal, TypeAlias, cast

RelationalDatabaseMetricName: TypeAlias = Literal[
    "CPUUtilization",
    "DatabaseConnections",
    "DiskQueueDepth",
    "FreeStorageSpace",
    "NetworkReceiveThroughput",
    "NetworkTransmitThroughput",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelationalDatabaseMetricName:
    return cast(RelationalDatabaseMetricName, data)
