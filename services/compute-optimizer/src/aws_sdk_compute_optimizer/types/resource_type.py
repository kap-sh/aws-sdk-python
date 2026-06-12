"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "Ec2Instance",
    "AutoScalingGroup",
    "EbsVolume",
    "LambdaFunction",
    "NotApplicable",
    "EcsService",
    "License",
    "RdsDBInstance",
    "AuroraDBClusterStorage",
    "Idle",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ec2Instance",
        "AutoScalingGroup",
        "EbsVolume",
        "LambdaFunction",
        "NotApplicable",
        "EcsService",
        "License",
        "RdsDBInstance",
        "AuroraDBClusterStorage",
        "Idle",
    )
)


def serialize_aws_json_1_0(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
