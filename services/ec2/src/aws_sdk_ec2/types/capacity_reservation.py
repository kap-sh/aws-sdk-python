"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_boolean
    import aws_sdk_ec2.types.capacity_allocations
    import aws_sdk_ec2.types.capacity_block_id
    import aws_sdk_ec2.types.capacity_reservation_commitment_info
    import aws_sdk_ec2.types.capacity_reservation_delivery_preference
    import aws_sdk_ec2.types.capacity_reservation_instance_platform
    import aws_sdk_ec2.types.capacity_reservation_state
    import aws_sdk_ec2.types.capacity_reservation_tenancy
    import aws_sdk_ec2.types.capacity_reservation_type
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.end_date_type
    import aws_sdk_ec2.types.instance_match_criteria
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.interruptible_capacity_allocation
    import aws_sdk_ec2.types.interruption_info
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.outpost_arn
    import aws_sdk_ec2.types.placement_group_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class CapacityReservation(TypedDict):
    capacity_reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the Capacity Reservation.</p>"""
    capacity_reservation_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Capacity Reservation.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone in which the capacity is reserved.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of instance for which the Capacity Reservation reserves capacity.</p>"""
    instance_platform: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_instance_platform.CapacityReservationInstancePlatform"
    ]
    """<p>The type of operating system for which the Capacity Reservation reserves capacity.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone in which the capacity is reserved.</p>"""
    tenancy: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_tenancy.CapacityReservationTenancy"
    ]
    """<p>Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:</p> <ul> <li> <p> <code>default</code> - The Capacity Reservation is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul>"""
    total_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of instances for which the Capacity Reservation reserves capacity.</p>"""
    available_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The remaining capacity. Indicates the number of instances that can be launched in the Capacity Reservation.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS- optimized instance.</p>"""
    ephemeral_storage: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> <i>Deprecated.</i> </p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_state.CapacityReservationState"
    ]
    """<p>The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:</p> <ul> <li> <p> <code>active</code> - The capacity is available for use.</p> </li> <li> <p> <code>expired</code> - The Capacity Reservation expired automatically at the date and time specified in your reservation request. The reserved capacity is no longer available for your use.</p> </li> <li> <p> <code>cancelled</code> - The Capacity Reservation was canceled. The reserved capacity is no longer available for your use.</p> </li> <li> <p> <code>pending</code> - The Capacity Reservation request was successful but the capacity provisioning is still pending.</p> </li> <li> <p> <code>failed</code> - The Capacity Reservation request has failed. A request can fail due to request parameters that are not valid, capacity constraints, or instance limit constraints. You can view a failed request for 60 minutes.</p> </li> <li> <p> <code>scheduled</code> - (<i>Future-dated Capacity Reservations</i>) The future-dated Capacity Reservation request was approved and the Capacity Reservation is scheduled for delivery on the requested start date.</p> </li> <li> <p> <code>payment-pending</code> - (<i>Capacity Blocks</i>) The upfront payment has not been processed yet.</p> </li> <li> <p> <code>payment-failed</code> - (<i>Capacity Blocks</i>) The upfront payment was not processed in the 12-hour time frame. Your Capacity Block was released.</p> </li> <li> <p> <code>assessing</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 is assessing your request for a future-dated Capacity Reservation.</p> </li> <li> <p> <code>delayed</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 encountered a delay in provisioning the requested future-dated Capacity Reservation. Amazon EC2 is unable to deliver the requested capacity by the requested start date and time.</p> </li> <li> <p> <code>unsupported</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 can't support the future-dated Capacity Reservation request due to capacity constraints. You can view unsupported requests for 30 days. The Capacity Reservation will not be delivered.</p> </li> </ul>"""
    start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time the Capacity Reservation was started.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to <code>expired</code> when it reaches its end date and time.</p>"""
    end_date_type: NotRequired["aws_sdk_ec2.types.end_date_type.EndDateType"]
    """<p>Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:</p> <ul> <li> <p> <code>unlimited</code> - The Capacity Reservation remains active until you explicitly cancel it.</p> </li> <li> <p> <code>limited</code> - The Capacity Reservation expires automatically at a specified date and time.</p> </li> </ul>"""
    instance_match_criteria: NotRequired[
        "aws_sdk_ec2.types.instance_match_criteria.InstanceMatchCriteria"
    ]
    """<p>Indicates the type of instance launches that the Capacity Reservation accepts. The options include:</p> <ul> <li> <p> <code>open</code> - The Capacity Reservation accepts all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes launch into the Capacity Reservation automatically without specifying any additional parameters.</p> </li> <li> <p> <code>targeted</code> - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity. </p> </li> </ul>"""
    create_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time the Capacity Reservation was created.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the Capacity Reservation.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.outpost_arn.OutpostArn"]
    """<p>The Amazon Resource Name (ARN) of the Outpost on which the Capacity Reservation was created.</p>"""
    capacity_reservation_fleet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation Fleet to which the Capacity Reservation belongs. Only valid for Capacity Reservations that were created by a Capacity Reservation Fleet.</p>"""
    placement_group_arn: NotRequired[
        "aws_sdk_ec2.types.placement_group_arn.PlacementGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the cluster placement group in which the Capacity Reservation was created. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html\"> Capacity Reservations for cluster placement groups</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    capacity_allocations: NotRequired[
        "aws_sdk_ec2.types.capacity_allocations.CapacityAllocations"
    ]
    """<p>Information about instance capacity usage.</p>"""
    reservation_type: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_type.CapacityReservationType"
    ]
    """<p>The type of Capacity Reservation.</p>"""
    unused_reservation_billing_owner_id: NotRequired[
        "aws_sdk_ec2.types.account_id.AccountID"
    ]
    """<p>The ID of the Amazon Web Services account to which billing of the unused capacity of the Capacity Reservation is assigned.</p>"""
    commitment_info: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_commitment_info.CapacityReservationCommitmentInfo"
    ]
    """<p>Information about your commitment for a future-dated Capacity Reservation.</p>"""
    delivery_preference: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_delivery_preference.CapacityReservationDeliveryPreference"
    ]
    """<p>The delivery method for a future-dated Capacity Reservation. <code>incremental</code> indicates that the requested capacity is delivered in addition to any running instances and reserved capacity that you have in your account at the requested date and time.</p>"""
    capacity_block_id: NotRequired[
        "aws_sdk_ec2.types.capacity_block_id.CapacityBlockId"
    ]
    """<p>The ID of the Capacity Block.</p>"""
    interruptible: NotRequired["aws_sdk_ec2.types.boxed_boolean.BoxedBoolean"]
    """<p> Indicates whether this Capacity Reservation is interruptible, meaning instances may be terminated when the owner reclaims capacity. </p>"""
    interruptible_capacity_allocation: NotRequired[
        "aws_sdk_ec2.types.interruptible_capacity_allocation.InterruptibleCapacityAllocation"
    ]
    """<p> Contains allocation details for interruptible reservations, including current allocated instances and target instance counts within the interruptibleCapacityAllocation object. </p>"""
    interruption_info: NotRequired[
        "aws_sdk_ec2.types.interruption_info.InterruptionInfo"
    ]
    """<p> Information about the interruption configuration and association with the source reservation for interruptible Capacity Reservations. </p>"""
