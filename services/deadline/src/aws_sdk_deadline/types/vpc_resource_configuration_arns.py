"""Generated from Smithy shape ``com.amazonaws.deadline#VpcResourceConfigurationArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.vpc_resource_configuration_arn

VpcResourceConfigurationArns: TypeAlias = list[
    "aws_sdk_deadline.types.vpc_resource_configuration_arn.VpcResourceConfigurationArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcResourceConfigurationArns) -> list:
    return list(value)


def deserialize_json(data: list) -> VpcResourceConfigurationArns:
    return list(data)
