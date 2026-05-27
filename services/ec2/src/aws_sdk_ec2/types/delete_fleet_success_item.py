"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetSuccessItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_id
    import aws_sdk_ec2.types.fleet_state_code


class DeleteFleetSuccessItem(TypedDict):
    current_fleet_state: NotRequired[
        "aws_sdk_ec2.types.fleet_state_code.FleetStateCode"
    ]
    """<p>The current state of the EC2 Fleet.</p>"""
    previous_fleet_state: NotRequired[
        "aws_sdk_ec2.types.fleet_state_code.FleetStateCode"
    ]
    """<p>The previous state of the EC2 Fleet.</p>"""
    fleet_id: NotRequired["aws_sdk_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""
