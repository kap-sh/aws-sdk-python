"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

RecommendationSourceType: TypeAlias = Literal[
    "Ec2Instance",
    "AutoScalingGroup",
    "EbsVolume",
    "LambdaFunction",
    "EcsService",
    "License",
    "RdsDBInstance",
    "RdsDBInstanceStorage",
    "AuroraDBClusterStorage",
    "NatGateway",
    "DynamoDBTable",
    "ElastiCacheCluster",
    "MemoryDBCluster",
    "DocumentDBCluster",
    "WorkSpaces",
    "SageMakerEndpoint",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ec2Instance",
        "AutoScalingGroup",
        "EbsVolume",
        "LambdaFunction",
        "EcsService",
        "License",
        "RdsDBInstance",
        "RdsDBInstanceStorage",
        "AuroraDBClusterStorage",
        "NatGateway",
        "DynamoDBTable",
        "ElastiCacheCluster",
        "MemoryDBCluster",
        "DocumentDBCluster",
        "WorkSpaces",
        "SageMakerEndpoint",
    )
)


def serialize_aws_json_1_0(value: RecommendationSourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RecommendationSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationSourceType value: {data!r}")
    return cast(RecommendationSourceType, data)
