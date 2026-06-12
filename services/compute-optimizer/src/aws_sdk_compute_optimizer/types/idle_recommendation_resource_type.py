"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendationResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

IdleRecommendationResourceType: TypeAlias = Literal[
    "EC2Instance",
    "AutoScalingGroup",
    "EBSVolume",
    "ECSService",
    "RDSDBInstance",
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
        "EC2Instance",
        "AutoScalingGroup",
        "EBSVolume",
        "ECSService",
        "RDSDBInstance",
        "NatGateway",
        "DynamoDBTable",
        "ElastiCacheCluster",
        "MemoryDBCluster",
        "DocumentDBCluster",
        "WorkSpaces",
        "SageMakerEndpoint",
    )
)


def serialize_aws_json_1_0(value: IdleRecommendationResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IdleRecommendationResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IdleRecommendationResourceType value: {data!r}"
        )
    return cast(IdleRecommendationResourceType, data)
