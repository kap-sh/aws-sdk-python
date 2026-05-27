"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unsuccessful_item

UnsuccessfulItemList: TypeAlias = list[
    "aws_sdk_ec2.types.unsuccessful_item.UnsuccessfulItem"
]
