"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Ec2AutoScalingGroupType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

Ec2AutoScalingGroupType: TypeAlias = Literal[
    "SingleInstanceType",
    "MixedInstanceTypes",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SingleInstanceType",
        "MixedInstanceTypes",
    )
)


def serialize_aws_json_1_0(value: Ec2AutoScalingGroupType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Ec2AutoScalingGroupType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Ec2AutoScalingGroupType value: {data!r}")
    return cast(Ec2AutoScalingGroupType, data)
