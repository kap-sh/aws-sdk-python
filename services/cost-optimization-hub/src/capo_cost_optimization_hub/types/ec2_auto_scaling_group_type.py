"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Ec2AutoScalingGroupType``."""

from typing import Literal, TypeAlias, cast

Ec2AutoScalingGroupType: TypeAlias = Literal[
    "SingleInstanceType",
    "MixedInstanceTypes",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2AutoScalingGroupType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Ec2AutoScalingGroupType:
    return cast(Ec2AutoScalingGroupType, data)
