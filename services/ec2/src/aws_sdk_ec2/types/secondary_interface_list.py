"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_interface

SecondaryInterfaceList: TypeAlias = list[
    "aws_sdk_ec2.types.secondary_interface.SecondaryInterface"
]
