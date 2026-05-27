"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFleetResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_fleet_errors_set
    import aws_sdk_ec2.types.create_fleet_instances_set
    import aws_sdk_ec2.types.fleet_id


class CreateFleetResult(TypedDict):
    fleet_id: NotRequired["aws_sdk_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC2 Fleet.</p>"""
    errors: NotRequired[
        "aws_sdk_ec2.types.create_fleet_errors_set.CreateFleetErrorsSet"
    ]
    """<p>Information about the instances that could not be launched by the fleet. Supported only for fleets of type <code>instant</code>.</p>"""
    instances: NotRequired[
        "aws_sdk_ec2.types.create_fleet_instances_set.CreateFleetInstancesSet"
    ]
    """<p>Information about the instances that were launched by the fleet. Supported only for fleets of type <code>instant</code>.</p>"""
