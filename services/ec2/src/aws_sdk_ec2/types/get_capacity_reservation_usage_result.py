"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityReservationUsageResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boxed_boolean
    import aws_sdk_ec2.types.capacity_reservation_state
    import aws_sdk_ec2.types.instance_usage_set
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.interruptible_capacity_allocation
    import aws_sdk_ec2.types.interruption_info
    import aws_sdk_ec2.types.string


class GetCapacityReservationUsageResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    capacity_reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of instance for which the Capacity Reservation reserves capacity.</p>"""
    total_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances for which the Capacity Reservation reserves capacity.</p>"""
    available_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The remaining capacity. Indicates the number of instances that can be launched in the Capacity Reservation.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_state.CapacityReservationState"
    ]
    """<p>The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:</p> <ul> <li> <p> <code>active</code> - The capacity is available for use.</p> </li> <li> <p> <code>expired</code> - The Capacity Reservation expired automatically at the date and time specified in your reservation request. The reserved capacity is no longer available for your use.</p> </li> <li> <p> <code>cancelled</code> - The Capacity Reservation was canceled. The reserved capacity is no longer available for your use.</p> </li> <li> <p> <code>pending</code> - The Capacity Reservation request was successful but the capacity provisioning is still pending.</p> </li> <li> <p> <code>failed</code> - The Capacity Reservation request has failed. A request can fail due to request parameters that are not valid, capacity constraints, or instance limit constraints. You can view a failed request for 60 minutes.</p> </li> <li> <p> <code>scheduled</code> - (<i>Future-dated Capacity Reservations</i>) The future-dated Capacity Reservation request was approved and the Capacity Reservation is scheduled for delivery on the requested start date.</p> </li> <li> <p> <code>payment-pending</code> - (<i>Capacity Blocks</i>) The upfront payment has not been processed yet.</p> </li> <li> <p> <code>payment-failed</code> - (<i>Capacity Blocks</i>) The upfront payment was not processed in the 12-hour time frame. Your Capacity Block was released.</p> </li> <li> <p> <code>assessing</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 is assessing your request for a future-dated Capacity Reservation.</p> </li> <li> <p> <code>delayed</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 encountered a delay in provisioning the requested future-dated Capacity Reservation. Amazon EC2 is unable to deliver the requested capacity by the requested start date and time.</p> </li> <li> <p> <code>unsupported</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 can't support the future-dated Capacity Reservation request due to capacity constraints. You can view unsupported requests for 30 days. The Capacity Reservation will not be delivered.</p> </li> </ul>"""
    instance_usages: NotRequired[
        "aws_sdk_ec2.types.instance_usage_set.InstanceUsageSet"
    ]
    """<p>Information about the Capacity Reservation usage.</p>"""
    interruptible: NotRequired["aws_sdk_ec2.types.boxed_boolean.BoxedBoolean"]
    """<p> Indicates whether the Capacity Reservation is interruptible, meaning instances may be terminated when the owner reclaims capacity. </p>"""
    interruptible_capacity_allocation: NotRequired[
        "aws_sdk_ec2.types.interruptible_capacity_allocation.InterruptibleCapacityAllocation"
    ]
    """<p> Information about the capacity allocated to the interruptible Capacity Reservation, including instance counts and allocation status. </p>"""
    interruption_info: NotRequired[
        "aws_sdk_ec2.types.interruption_info.InterruptionInfo"
    ]
    """<p> Details about the interruption configuration and source reservation for interruptible Capacity Reservations. </p>"""
