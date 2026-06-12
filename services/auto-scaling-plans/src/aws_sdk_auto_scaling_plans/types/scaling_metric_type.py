"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalingMetricType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: ScalingMetricType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingMetricType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalingMetricType value: {data!r}")
    return cast(ScalingMetricType, data)
