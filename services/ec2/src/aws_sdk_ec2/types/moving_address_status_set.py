"""Generated from Smithy shape ``com.amazonaws.ec2#MovingAddressStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.moving_address_status

MovingAddressStatusSet: TypeAlias = list[
    "aws_sdk_ec2.types.moving_address_status.MovingAddressStatus"
]
