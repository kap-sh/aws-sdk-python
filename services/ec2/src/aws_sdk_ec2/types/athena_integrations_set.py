"""Generated from Smithy shape ``com.amazonaws.ec2#AthenaIntegrationsSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.athena_integration

AthenaIntegrationsSet: TypeAlias = list[
    "aws_sdk_ec2.types.athena_integration.AthenaIntegration"
]
