"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetErrorItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_fleet_error
    import aws_sdk_ec2.types.fleet_id


class DeleteFleetErrorItem(TypedDict):
    error: NotRequired["aws_sdk_ec2.types.delete_fleet_error.DeleteFleetError"]
    """<p>The error.</p>"""
    fleet_id: NotRequired["aws_sdk_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""
