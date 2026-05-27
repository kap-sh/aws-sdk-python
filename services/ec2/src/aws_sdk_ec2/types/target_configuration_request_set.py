"""Generated from Smithy shape ``com.amazonaws.ec2#TargetConfigurationRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.target_configuration_request

TargetConfigurationRequestSet: TypeAlias = list[
    "aws_sdk_ec2.types.target_configuration_request.TargetConfigurationRequest"
]
