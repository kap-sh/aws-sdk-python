"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_secondary_interface

InstanceSecondaryInterfaceList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_secondary_interface.InstanceSecondaryInterface"
]
