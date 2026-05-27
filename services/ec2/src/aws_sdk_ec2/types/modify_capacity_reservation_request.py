"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyCapacityReservationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.end_date_type
    import aws_sdk_ec2.types.instance_match_criteria
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class ModifyCapacityReservationRequest(TypedDict):
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances for which to reserve capacity. The number of instances can't be increased or decreased by more than <code>1000</code> in a single request.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to <code>expired</code> when it reaches its end date and time.</p> <p>The Capacity Reservation is cancelled within an hour from the specified time. For example, if you specify 5/31/2019, 13:30:55, the Capacity Reservation is guaranteed to end between 13:30:55 and 14:30:55 on 5/31/2019.</p> <p>You must provide an <code>EndDate</code> value if <code>EndDateType</code> is <code>limited</code>. Omit <code>EndDate</code> if <code>EndDateType</code> is <code>unlimited</code>.</p>"""
    end_date_type: NotRequired["aws_sdk_ec2.types.end_date_type.EndDateType"]
    """<p>Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:</p> <ul> <li> <p> <code>unlimited</code> - The Capacity Reservation remains active until you explicitly cancel it. Do not provide an <code>EndDate</code> value if <code>EndDateType</code> is <code>unlimited</code>.</p> </li> <li> <p> <code>limited</code> - The Capacity Reservation expires automatically at a specified date and time. You must provide an <code>EndDate</code> value if <code>EndDateType</code> is <code>limited</code>.</p> </li> </ul>"""
    accept: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Reserved. Capacity Reservations you have created are accepted by default.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    additional_info: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved for future use.</p>"""
    instance_match_criteria: NotRequired[
        "aws_sdk_ec2.types.instance_match_criteria.InstanceMatchCriteria"
    ]
    """<p> The matching criteria (instance eligibility) that you want to use in the modified Capacity Reservation. If you change the instance eligibility of an existing Capacity Reservation from <code>targeted</code> to <code>open</code>, any running instances that match the attributes of the Capacity Reservation, have the <code>CapacityReservationPreference</code> set to <code>open</code>, and are not yet running in the Capacity Reservation, will automatically use the modified Capacity Reservation. </p> <p>To modify the instance eligibility, the Capacity Reservation must be completely idle (zero usage).</p>"""
