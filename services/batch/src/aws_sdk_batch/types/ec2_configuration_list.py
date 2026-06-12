"""Generated from Smithy shape ``com.amazonaws.batch#Ec2ConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.ec2_configuration

Ec2ConfigurationList: TypeAlias = list[
    "aws_sdk_batch.types.ec2_configuration.Ec2Configuration"
]


# --- restJson1 ser/de ---
def serialize_json(value: Ec2ConfigurationList) -> list:
    import aws_sdk_batch.types.ec2_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.ec2_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> Ec2ConfigurationList:
    import aws_sdk_batch.types.ec2_configuration

    out: Ec2ConfigurationList = []
    for item in data:
        out.append(aws_sdk_batch.types.ec2_configuration.deserialize_json(item))
    return out
