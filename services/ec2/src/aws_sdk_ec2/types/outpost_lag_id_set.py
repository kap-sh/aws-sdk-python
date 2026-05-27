"""Generated from Smithy shape ``com.amazonaws.ec2#OutpostLagIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.outpost_lag_id

OutpostLagIdSet: TypeAlias = list["aws_sdk_ec2.types.outpost_lag_id.OutpostLagId"]
