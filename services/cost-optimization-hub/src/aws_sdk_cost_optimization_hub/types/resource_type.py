"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "Ec2Instance",
    "LambdaFunction",
    "EbsVolume",
    "EcsService",
    "Ec2AutoScalingGroup",
    "Ec2InstanceSavingsPlans",
    "ComputeSavingsPlans",
    "SageMakerSavingsPlans",
    "Ec2ReservedInstances",
    "RdsReservedInstances",
    "OpenSearchReservedInstances",
    "RedshiftReservedInstances",
    "ElastiCacheReservedInstances",
    "RdsDbInstanceStorage",
    "RdsDbInstance",
    "AuroraDbClusterStorage",
    "DynamoDbReservedCapacity",
    "MemoryDbReservedInstances",
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
        "LambdaFunction",
        "EbsVolume",
        "EcsService",
        "Ec2AutoScalingGroup",
        "Ec2InstanceSavingsPlans",
        "ComputeSavingsPlans",
        "SageMakerSavingsPlans",
        "Ec2ReservedInstances",
        "RdsReservedInstances",
        "OpenSearchReservedInstances",
        "RedshiftReservedInstances",
        "ElastiCacheReservedInstances",
        "RdsDbInstanceStorage",
        "RdsDbInstance",
        "AuroraDbClusterStorage",
        "DynamoDbReservedCapacity",
        "MemoryDbReservedInstances",
        "NatGateway",
        "DynamoDBTable",
        "ElastiCacheCluster",
        "MemoryDBCluster",
        "DocumentDBCluster",
        "WorkSpaces",
        "SageMakerEndpoint",
    )
)


def serialize_aws_json_1_0(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
