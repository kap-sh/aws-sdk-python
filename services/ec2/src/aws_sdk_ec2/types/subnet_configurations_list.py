"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_configuration

SubnetConfigurationsList: TypeAlias = list[
    "aws_sdk_ec2.types.subnet_configuration.SubnetConfiguration"
]
