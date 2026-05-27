"""Generated from Smithy shape ``com.amazonaws.ec2#OccurrenceDayRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer

OccurrenceDayRequestSet: TypeAlias = list["aws_sdk_ec2.types.integer.Integer"]
