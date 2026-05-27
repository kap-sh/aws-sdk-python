"""Generated from Smithy shape ``com.amazonaws.ec2#AssociatedTargetNetworkSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associated_target_network

AssociatedTargetNetworkSet: TypeAlias = list[
    "aws_sdk_ec2.types.associated_target_network.AssociatedTargetNetwork"
]
