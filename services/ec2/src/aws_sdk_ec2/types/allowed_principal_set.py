"""Generated from Smithy shape ``com.amazonaws.ec2#AllowedPrincipalSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allowed_principal

AllowedPrincipalSet: TypeAlias = list[
    "aws_sdk_ec2.types.allowed_principal.AllowedPrincipal"
]
