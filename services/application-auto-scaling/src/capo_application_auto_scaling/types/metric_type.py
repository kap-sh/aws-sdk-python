"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#MetricType``."""

from typing import Literal, TypeAlias, cast

MetricType: TypeAlias = Literal[
    "DynamoDBReadCapacityUtilization",
    "DynamoDBWriteCapacityUtilization",
    "ALBRequestCountPerTarget",
    "RDSReaderAverageCPUUtilization",
    "RDSReaderAverageDatabaseConnections",
    "EC2SpotFleetRequestAverageCPUUtilization",
    "EC2SpotFleetRequestAverageNetworkIn",
    "EC2SpotFleetRequestAverageNetworkOut",
    "SageMakerVariantInvocationsPerInstance",
    "ECSServiceAverageCPUUtilization",
    "ECSServiceAverageMemoryUtilization",
    "AppStreamAverageCapacityUtilization",
    "ComprehendInferenceUtilization",
    "LambdaProvisionedConcurrencyUtilization",
    "CassandraReadCapacityUtilization",
    "CassandraWriteCapacityUtilization",
    "KafkaBrokerStorageUtilization",
    "ElastiCacheEngineCPUUtilization",
    "ElastiCacheDatabaseMemoryUsagePercentage",
    "ElastiCachePrimaryEngineCPUUtilization",
    "ElastiCacheReplicaEngineCPUUtilization",
    "ElastiCacheDatabaseMemoryUsageCountedForEvictPercentage",
    "NeptuneReaderAverageCPUUtilization",
    "SageMakerVariantProvisionedConcurrencyUtilization",
    "ElastiCacheDatabaseCapacityUsageCountedForEvictPercentage",
    "SageMakerInferenceComponentInvocationsPerCopy",
    "WorkSpacesAverageUserSessionsCapacityUtilization",
    "SageMakerInferenceComponentConcurrentRequestsPerCopyHighResolution",
    "SageMakerVariantConcurrentRequestsPerModelHighResolution",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricType:
    return cast(MetricType, data)
