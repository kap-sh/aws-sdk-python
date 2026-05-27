"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCapacityReservationAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_specification
    import aws_sdk_ec2.types.instance_id


class ModifyInstanceCapacityReservationAttributesRequest(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance to be modified.</p>"""
    capacity_reservation_specification: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_specification.CapacityReservationSpecification"
    ]
    """<p>Information about the Capacity Reservation targeting option.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
