"""Generated from Smithy shape ``com.amazonaws.ec2#AddedPrincipalSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.added_principal

AddedPrincipalSet: TypeAlias = list["aws_sdk_ec2.types.added_principal.AddedPrincipal"]
