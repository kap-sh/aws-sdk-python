"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetSuccessSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_fleet_success_item

DeleteFleetSuccessSet: TypeAlias = list[
    "aws_sdk_ec2.types.delete_fleet_success_item.DeleteFleetSuccessItem"
]
