"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulItemSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unsuccessful_item

UnsuccessfulItemSet: TypeAlias = list[
    "aws_sdk_ec2.types.unsuccessful_item.UnsuccessfulItem"
]
