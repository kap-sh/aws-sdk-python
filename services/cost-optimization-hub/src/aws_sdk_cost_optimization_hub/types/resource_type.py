"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ResourceType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceType:
    return cast(ResourceType, data)
