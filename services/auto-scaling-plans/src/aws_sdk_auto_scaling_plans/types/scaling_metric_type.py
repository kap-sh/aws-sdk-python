"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingMetricType``."""

from typing import Literal, TypeAlias, cast

ScalingMetricType: TypeAlias = Literal[
    "ASGAverageCPUUtilization",
    "ASGAverageNetworkIn",
    "ASGAverageNetworkOut",
    "DynamoDBReadCapacityUtilization",
    "DynamoDBWriteCapacityUtilization",
    "ECSServiceAverageCPUUtilization",
    "ECSServiceAverageMemoryUtilization",
    "ALBRequestCountPerTarget",
    "RDSReaderAverageCPUUtilization",
    "RDSReaderAverageDatabaseConnections",
    "EC2SpotFleetRequestAverageCPUUtilization",
    "EC2SpotFleetRequestAverageNetworkIn",
    "EC2SpotFleetRequestAverageNetworkOut",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingMetricType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingMetricType:
    return cast(ScalingMetricType, data)
