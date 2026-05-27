"""Generated from Smithy shape ``com.amazonaws.ec2#TargetNetworkSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.target_network

TargetNetworkSet: TypeAlias = list["aws_sdk_ec2.types.target_network.TargetNetwork"]
