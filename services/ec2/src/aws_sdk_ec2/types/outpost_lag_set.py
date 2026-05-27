"""Generated from Smithy shape ``com.amazonaws.ec2#OutpostLagSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.outpost_lag

OutpostLagSet: TypeAlias = list["aws_sdk_ec2.types.outpost_lag.OutpostLag"]
