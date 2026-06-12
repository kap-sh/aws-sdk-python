"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ScalableDimension``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

ScalableDimension: TypeAlias = Literal[
    "autoscaling:autoScalingGroup:DesiredCapacity",
    "ecs:service:DesiredCount",
    "ec2:spot-fleet-request:TargetCapacity",
    "rds:cluster:ReadReplicaCount",
    "dynamodb:table:ReadCapacityUnits",
    "dynamodb:table:WriteCapacityUnits",
    "dynamodb:index:ReadCapacityUnits",
    "dynamodb:index:WriteCapacityUnits",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "autoscaling:autoScalingGroup:DesiredCapacity",
        "ecs:service:DesiredCount",
        "ec2:spot-fleet-request:TargetCapacity",
        "rds:cluster:ReadReplicaCount",
        "dynamodb:table:ReadCapacityUnits",
        "dynamodb:table:WriteCapacityUnits",
        "dynamodb:index:ReadCapacityUnits",
        "dynamodb:index:WriteCapacityUnits",
    )
)


def serialize_aws_json_1_1(value: ScalableDimension) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalableDimension:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalableDimension value: {data!r}")
    return cast(ScalableDimension, data)
