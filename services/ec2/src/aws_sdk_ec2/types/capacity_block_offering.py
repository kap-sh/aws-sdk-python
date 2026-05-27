"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockOffering``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boxed_integer
    import aws_sdk_ec2.types.capacity_reservation_tenancy
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.offering_id
    import aws_sdk_ec2.types.string


class CapacityBlockOffering(TypedDict):
    capacity_block_offering_id: NotRequired["aws_sdk_ec2.types.offering_id.OfferingId"]
    """<p>The ID of the Capacity Block offering.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type of the Capacity Block offering.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone of the Capacity Block offering.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances in the Capacity Block offering.</p>"""
    start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date of the Capacity Block offering.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The end date of the Capacity Block offering.</p>"""
    capacity_block_duration_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of hours (in addition to <code>capacityBlockDurationMinutes</code>) for the duration of the Capacity Block reservation. For example, if a Capacity Block starts at <b>04:55</b> and ends at <b>11:30</b>, the hours field would be <b>6</b>.</p>"""
    upfront_fee: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The total price to be paid up front.</p>"""
    currency_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The currency of the payment for the Capacity Block.</p>"""
    tenancy: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_tenancy.CapacityReservationTenancy"
    ]
    """<p>The tenancy of the Capacity Block.</p>"""
    ultraserver_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The EC2 UltraServer type of the Capacity Block offering.</p>"""
    ultraserver_count: NotRequired["aws_sdk_ec2.types.boxed_integer.BoxedInteger"]
    """<p>The number of EC2 UltraServers in the offering.</p>"""
    capacity_block_duration_minutes: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of minutes (in addition to <code>capacityBlockDurationHours</code>) for the duration of the Capacity Block reservation. For example, if a Capacity Block starts at <b>08:55</b> and ends at <b>11:30</b>, the minutes field would be <b>35</b>.</p>"""
    zone_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of zone where the Capacity Block offering is available.</p>"""
