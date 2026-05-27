"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_fleet_error_item

DeleteFleetErrorSet: TypeAlias = list[
    "aws_sdk_ec2.types.delete_fleet_error_item.DeleteFleetErrorItem"
]
