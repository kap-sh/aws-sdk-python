"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceConfigurationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_configuration

ServiceConfigurationSet: TypeAlias = list[
    "aws_sdk_ec2.types.service_configuration.ServiceConfiguration"
]
